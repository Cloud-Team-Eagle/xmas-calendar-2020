

puts "hello from ruby"





# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz

# raise "error" unless fizz_buzz(10) == ['1', ...]


raise "error for..." unless fizz_buzz_for_id(1) == "1"
raise "error for..." unless fizz_buzz_for_id(3) == "fizz"
raise "error for..." unless fizz_buzz_for_id(15) == "fizz buzz"


def fizz_buzz(max=10)
	[1..max].each { |it| fizz_buzz_for_id(it) }
end


def fizz_buzz_for_id(id)

end
