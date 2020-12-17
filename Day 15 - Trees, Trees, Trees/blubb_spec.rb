require_relative 'blubb.rb'

RSpec.describe "blubb" do
  describe '#blubb' do
    it "blubb blubb" do
      expect(Greeter.new.greet).to eq("Hello, world!")
    end
  end
end



# Input: Postfix expression:  A B + 
# Output: Prefix expression- + A B

# Input: Postfix expression:  ABC/-AK/L-*
# Output: Infix expression: *-A/BC-/AKL


