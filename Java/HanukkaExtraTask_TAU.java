public class HanukkaChallenge {
	// we need to sum the candles used in 8 days of Hanukka
	// every day we light 1 shamash + X candles according to the day number
	
	// begginers
	// we create a counter
	// we add 8 times 1 + dayNumber (which starts from 1 and increases every time)
	
	// mid level
	public static int sum_the_candles() {
		// we create a counter
		int sum = 0;
	
		// we add 8 times 1 + dayNumber (which starts from 1 and increases every time)
		for (int dayNumber = 1; dayNumber <= 8; dayNumber++) {
			sum += 1 + dayNumber;
		}
			
		return sum;
	}
	
	// expert
	// create another func to print the candles
	// use | for the candles
	// use ! for the shamash
	public static void let_there_be_light() {
		String result;
	
		for (int dayNumber = 1; dayNumber <= 8; dayNumber++) {
			// to print just 1 line for each day we'll use a var to save our Menorah
			// and initialize it with the shamash
			result = "!";
			// for evety day passed we'll light a candle
			for (int i=0; i<dayNumber; i++)
				result += " |";
			// for the remaining days we leave a place in our Menorah
			for (int i=0; i<8-dayNumber; i++)
				result += " _";
			// and then we print the complite Menorah
			System.out.println(result);
		}
	}
			
        
     public static void main(String []args){
        System.out.println(sum_the_candles());
        let_there_be_light();
     }
}