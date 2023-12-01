begin
    file = File.open("example1.txt", "r")
    numbers = Array.new

    file.each_line do |line|
        aux = Array.new()
        line.each_char do |char|
            if char.to_i != 0
                aux.push(char)
            end
        end
        numbers.push([aux[0], aux[aux.length-1]].join)
    end
    file.close()
    
    sum = numbers.map(&:to_i).reduce(:+)
    puts "The sum is: #{sum}"
end