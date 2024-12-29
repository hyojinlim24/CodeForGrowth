class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle the edge case where x is 0
        if x == 0:
            return 0
        
        # Start with an initial guess (half of x)
        last_guess = x / 2.0
        
        # Iteratively improve the guess
        while True:
            # Calculate the new guess using Newton's method
            guess = (last_guess + x / last_guess) / 2
            
            # If the difference between the current and previous guess is very small, break the loop
            if abs(guess - last_guess) < 0.000001:
                return int(guess)  # Return the integer part of the guess
            
            # Update last_guess for the next iteration
            last_guess = guess