
def BracketMatcher(str)
  stack = []

  str.chars.each { |char|
    case char
    when "("
      stack.push(char)
    when "["
      stack.push(char)
    when ")"
      return 0 if stack.pop != "("
    when "]"
      return 0 if stack.pop != "["
    end
  }

  if len(stack) != 0
    return 0
  end
  
  return 1
end




