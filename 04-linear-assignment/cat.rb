require "rmagick"

image = Magick::Image.read("cat.jpg").first
block_size = 25

width = image.columns
height = image.rows

mosaic = Magick::Image.new(width, height)
pencil = Magick::Draw.new

num_columns = width / block_size
num_rows = height / block_size

num_rows.times do |block_y|
  num_columns.times do |block_x|
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

    brightness = sum / (block_size * block_size) / 3

    #pencil.fill("blue")
    #pencil.rectangle(50, 50, 250, 250)
    #pencil.draw(mosaic)

    puts "Block #{block_x}, #{block_y} has brightness #{brightness}"
  end
end

mosaic.write("mosaic.jpg")
