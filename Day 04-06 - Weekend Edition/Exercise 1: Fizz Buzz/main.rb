

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


def fizz_buzz(max=10)
	[1..max].each { |it| fizz_buzz_for_id(it) }
end


def fizz_buzz_for_id(id)

end



# raise "error" unless fizz_buzz(10) == ['1', ...]

raise "error for 1..." unless fizz_buzz_for_id(1) == "1"
raise "error for 2..." unless fizz_buzz_for_id(3) == "fizz"
raise "error for 3..." unless fizz_buzz_for_id(15) == "fizz buzz"

