require "rmagick"

image = Magick::Image.read("cat.jpg").first
block_size = 25
num_cartoons = 8

width = image.columns
height = image.rows

mosaic = Magick::Image.new(width, height)
pencil = Magick::Draw.new

num_columns = width / block_size
num_rows = height / block_size

total_blocks = num_columns * num_rows
num_of_each_cartoon = total_blocks / num_columns

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

lp.close

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
