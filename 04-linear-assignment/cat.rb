require "rmagick"

image = Magick::Image.read("cat.jpg").first
block_size = 57
num_cartoons = 8

width = image.columns
height = image.rows

mosaic = Magick::Image.new(width, height)
pencil = Magick::Draw.new

num_columns = width / block_size
num_rows = height / block_size

num_variables = num_cartoons * num_columns * num_rows
puts "There are #{num_variables} variables (2000 are allowed)"

total_blocks = num_columns * num_rows
num_of_each_cartoon = (total_blocks.to_f / num_cartoons).floor

puts "There are #{total_blocks} blocks in total."
puts "And we have #{num_cartoons} cartoons."
puts "So there will be #{num_of_each_cartoon} of each each cartoon."

brightness_values = num_rows.times.map do |block_y|
  num_columns.times.map do |block_x|
    sum = 0

    (0...block_size).each do |pixel_y|
      (0...block_size).each do |pixel_x|
        y_offset = block_y * block_size + pixel_y
        x_offset = block_x * block_size + pixel_x

        pixel = image.pixel_color(x_offset, y_offset)

        sum += pixel.red.to_f / 255 / 255 # Between 0 and 1.
        sum += pixel.green.to_f / 255 / 255
        sum += pixel.blue.to_f / 255 / 255
      end
    end

    sum / (block_size * block_size) / 3
  end
end

#puts brightness_values.inspect

lp = File.open("mosaic.lp", "w")
lp.puts "minimize"

puts "Minimize the total cost of putting each cartoon in each grid cell:"
step = 1.0 / (num_cartoons - 1)
terms = []
num_cartoons.times do |cartoon|
  cartoon_brightness = step * cartoon

  num_rows.times do |y|
    num_columns.times do |x|
      delta = (cartoon_brightness - brightness_values[y][x]) ** 2
      terms.push("#{delta} cartoon_#{cartoon}_y_#{y}_x_#{x}")
    end
  end
end
lp.puts "  #{terms.join(" + ")}"

lp.puts "subject to"

puts "There has to be exactly one cartoon in each block:"
num_rows.times do |y|
  num_columns.times do |x|
    terms = []

    num_cartoons.times do |cartoon|
      terms.push("cartoon_#{cartoon}_y_#{y}_x_#{x}")
    end

    lp.puts "  #{terms.join(" + ")} == 1"
  end
end

lp.puts

puts "There has to be at least #{num_of_each_cartoon} of each cartoon in the mosaic."
num_cartoons.times do |cartoon|
  terms = []

  num_rows.times do |y|
    num_columns.times do |x|
      terms.push("cartoon_#{cartoon}_y_#{y}_x_#{x}")
    end
  end

  lp.puts "  #{terms.join(" + ")} >= #{num_of_each_cartoon}"
end

lp.puts "integers"
puts "Each cartoon can either appear or not appear in each grid cell:"
num_cartoons.times do |cartoon|
  num_rows.times do |y|
    num_columns.times do |x|
      lp.puts "  cartoon_#{cartoon}_y_#{y}_x_#{x}"
    end
  end
end

lp.puts "end"
lp.close

puts "Running solver..."
result = `gurobi_cl Resultfile=mosaic.sol Logfile=mosaic.log Method=0 mosaic.lp`
success = result.include?("Wrote result file 'mosaic.sol'")

if success
  puts "Solved successfully!"
else
  puts "Failed to find a solution"
  exit 1
end


#left = block_x * block_size
#top = block_y * block_size
#right = left + block_size
#bottom = top + block_size
#
#pencil.rectangle(left, top, right, bottom)
#
#pencil.draw(mosaic)
#mosaic.write("mosaic.jpg")
#
