# Questions to assess JAVA skills
- TekArchWebPortal
- Questions from: Divya Shree and Balu S
- Responses from: Jasvinder Ahuja

_To upload the solution. Keep question, solution, input and output of all the problems in a single PDF file and upload it. (you can put it in a document and convert into PDF format. use any online converter)_

## 1)Write a Java program to print the result of the following operations.(no need to read data from user)
Test Data:
- a. -5 + 8 * 6
- b. (55+9) % 9
- c. 20 + -3*5 / 8
- d. 5 + 15 / 3 * 2 - 8 % 3
    - Expected Output :4311913


```Java
public class Operation_a {
    public static void main(String[] args) {
        int a = -5;
        int b = 8;
        int c = 6;
        int d = a+b*c;
        System.out.println("a+b*c = " + d);
        }
}
```


```Java
Operation_a.main(new String[]{})
```

    a+b*c = 43



```Java
System.out.println("b. (55+9) % 9 = " + ((55+9) % 9));
```

    b. (55+9) % 9 = 1



```Java
System.out.println("c. 20 + -3*5 / 8 = "+ (20+ (-3*5)/8))
```

    c. 20 + -3*5 / 8 = 19



```Java
System.out.println("d. 5 + 15 / 3 * 2 - 8 % 3 = " +(5 + 15 / 3 * 2 - 8 % 3))
```

    d. 5 + 15 / 3 * 2 - 8 % 3 = 13


## 2)Write a Java program to compute a specified formula.

- Specified Formula :4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))
- Expected Output 2.9760461760461765


```Java
public class compute_2{
    public static void main (String[] args){
        double res =  (4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11)));
        System.out.println("2. 4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11)) = " + res );
    }
}
```


```Java
compute_2.main(new String[]{})
```

    2. 4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11)) = 2.9760461760461765


## 3)Write a Java program that takes a number as input(read it from user) and prints its multiplication table upto 10.
Test Data:
- Input a number: 8
- Expected Output:  
    * 8 x 1 = 8  
    * 8 x 2 = 16  
    * 8 x 3 = 24...  
    *  
    *  
    * 8 x 10 = 80  


```Java
import java.util.Scanner;
public class TimesTables{
    public static void calcTable(int a){
        System.out.println("Multiplication table for number: "+ a);
        for(int i=1; i<=10; i++){
            System.out.println(a+" * "+i+" = "+(a*i));
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number to generate its multiplication table: ");
        int number = scanner.nextInt();
        
        calcTable(number);
        
        scanner.close();
    }
}
```


```Java
TimesTables.main(new String[]{})
```

    Enter a number to generate its multiplication table: 

     12


    Multiplication table for number: 12
    12 * 1 = 12
    12 * 2 = 24
    12 * 3 = 36
    12 * 4 = 48
    12 * 5 = 60
    12 * 6 = 72
    12 * 7 = 84
    12 * 8 = 96
    12 * 9 = 108
    12 * 10 = 120


## 4)Write a Java program to print the sum (addition), multiply, subtract, divide and remainder of two numbers(read two numbers from user).

- Test Data:  
    - Input first number: 125  
    - Input second number: 24  
    - Expected Output:   
        125 + 24 = 149  
        125 - 24 = 101  
        125 x 24 = 3000  
        125 / 24 = 5  
        125 mod 24 = 5  


```Java
import java.util.Scanner;
public class MyMath {
    public static int sumNs(int a, int b) {
        return a + b;
    }
    public static int multiplyNs(int a, int b) {
        return a * b;
    }
    public static int subtractNs(int a, int b) {
        return a - b;
    }
    public static int divideNs(int a, int b) {
        if(b==0){
            System.out.println("Error divisor is 0");
            return 0;
        }
        return a / b;
    }
    public static int remainderNs(int a, int b) {
        return a % b;
    }
    public static int [] returnAll(int a, int b) {
        return new int [] {sumNs(a, b), multiplyNs(a, b), subtractNs(a, b), divideNs(a, b), remainderNs(a, b)};
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number `a`: ");
        int m = scanner.nextInt();

        System.out.print("Enter another number `b`: ");
        int n = scanner.nextInt();
        
        int[] results = returnAll(m, n);

        // Print results
        System.out.println("\nResults:");
        System.out.println("Sum (a+b): " + results[0]);
        System.out.println("Multiplication (a*b): " + results[1]);
        System.out.println("Subtraction (a-b): " + results[2]);
        System.out.println("Division (a/b): " + results[3]);
        System.out.println("Remainder (a%b) : " + results[4]);

        scanner.close();
    }
}
```


```Java
MyMath.main(new String[]{})
```

    Enter a number `a`: 

     12


    Enter another number `b`: 

     23


    
    Results:
    Sum (a+b): 35
    Multiplication (a*b): 276
    Subtraction (a-b): -11
    Division (a/b): 0
    Remainder (a%b) : 12


## 5)Write a Java program that takes three numbers as input to calculate and print the average of the three numbers


```Java
import java.util.Scanner;
public class MyAverageOfThree{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number `a`: ");
        int a = scanner.nextInt();

        System.out.print("Enter another number `b`: ");
        int b = scanner.nextInt();

        System.out.print("Enter another number `c`: ");
        int c = scanner.nextInt();

        System.out.println("Average of "+a+","+b+","+c+" is "+ (a+b+c)/3);
        scanner.close();
        
    }
}
```


```Java
MyAverageOfThree.main(new String[]{})
```

    Enter a number `a`: 

     12


    Enter another number `b`: 

     23


    Enter another number `c`: 

     34


    Average of 12,23,34 is 23



```Java
import java.util.Scanner;

public class MyAverageOfThree_ArrayVersion {
    public static double calculateAverage(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return (double) sum / numbers.length;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int[] numbers = new int[3];

        for(int i = 0; i<3; i++){

            System.out.print("Enter a number "+(i+1)+" :");
            numbers[i] = scanner.nextInt();
        }
        
        double average = calculateAverage(numbers);
        System.out.println("Average of " + numbers[0] + ", " + numbers[1] + ", and " + numbers[2] + " = " + average);

        scanner.close();
    }
}
```


```Java
MyAverageOfThree_ArrayVersion.main(new String[]{})
```

    Enter a number 1 :

     12


    Enter a number 2 :

     23


    Enter a number 3 :

     34


    Average of 12, 23, and 34 = 23.0


## 6)Write a Java program to convert a decimal number to binary number.
- input : 5
- output:101


```Java
public class DecimalToBinary {

    // Recursive method to convert a decimal number to binary
    public static String deciToBinary(int num) {
        if (num == 0) {
            return "0";
        }
        if (num == 1) {
            return "1";
        }
        return deciToBinary(num / 2) + (num % 2);
    }

    public static void main(String[] args) {
        int example_num = 10;

        String binary = deciToBinary(example_num);
        System.out.println("Binary representation of " + example_num + " is: " + binary);
    }
}

```


```Java
DecimalToBinary.deciToBinary(10)
```




    1010



## 7)Write a Java program and compute the sum of the digits of an integer.
- input: 234
- note: 2+3+4=9
- so output:9 


```Java
import java.util.Scanner;

public class SumOfDigits {
    public static int sumDigits(int num) {
        // Base case
        if (num == 0) {
            return 0;
        }
        // Recursive case
        return (num % 10) + sumDigits(num / 10);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int input_num = scanner.nextInt();

        // Call the recursive method
        int res = sumDigits(input_num);

        System.out.println("Sum of digits: " + res);

        scanner.close();
    }
}

```


```Java
SumOfDigits.sumDigits(10101)
```




    3



## 8)Write a Java program to convert float to double and convert double to float


```Java
import java.util.Scanner;

public class floatsNDoubles {
    public static double flToDbl(float fltVal) {
        return (double) fltVal;
    }

    public static float dblToFlt(double dblVal) {
        return (float) dblVal;
    }
    /* Main method first asks which conversion is needed 
    then performs the desired conversion.
    */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose the conversion you want to perform:");
        System.out.println("1. Convert float to double");
        System.out.println("2. Convert double to float");
        System.out.print("Enter your choice (1 or 2): ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.print("Enter a float value: ");
            float inputFlt = scanner.nextFloat();
            double convertedDbl = flToDbl(inputFlt);
            System.out.println("Converted float to double: " + convertedDbl);
        } else if (choice == 2) {
            System.out.print("Enter a double value: ");
            double inputDbl = scanner.nextDouble();
            float convertedFlt = dblToFlt(inputDbl);
            System.out.println("Converted double to float: " + convertedFlt);
        } else {
            System.out.println("Invalid choice! Please enter 1 or 2.");
        }

        scanner.close();
    }
}

```


```Java
// Oh I forgot in jupyter notebook we need to use: new String[]{}
floatsNDoubles.main(new String[]{})
```

    Choose the conversion you want to perform:
    1. Convert float to double
    2. Convert double to float
    Enter your choice (1 or 2): 

     1


    Enter a float value: 

     1.11


    Converted float to double: 1.1100000143051147



```Java
floatsNDoubles.main(new String[]{})
```

    Choose the conversion you want to perform:
    1. Convert float to double
    2. Convert double to float
    Enter your choice (1 or 2): 

     2


    Enter a double value: 

     1.1111111


    Converted double to float: 1.111111


## 9)Write a Java program to print today’s date and time.


```Java
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeExample {

    public static LocalDateTime getCurrentDateTime() {
        return LocalDateTime.now();
    }

    public static String formatDateTime(LocalDateTime dateTime) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return dateTime.format(formatter);
    }

    public static void main(String[] args) {
        LocalDateTime dateTimeNow = getCurrentDateTime();
        String formattedDateTime = formatDateTime(dateTimeNow);
        System.out.println("Formatted Date and Time: " + formattedDateTime);
    }
}
```


```Java
DateTimeExample.main(new String[]{})
```

    Formatted Date and Time: 2024-09-07 09:05:16


## 10)Write a Java program to print today’s date in the format DD/MM/yyyy 


```Java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DateFormatExample {

    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String formattedDate = today.format(formatter);
        System.out.println("Today's Date in DD/MM/yyyy format: " + formattedDate);
    }
}
```


```Java
DateFormatExample.main(new String[]{})
```

    Today's Date in DD/MM/yyyy format: 07/09/2024


## 11)Write A Java program to print current time in the format hh:mm:ss with time zone.
-Ex : 03:15:45 PST


```Java
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

public class TimeFormatExample {
    public static String getTimeWithTimeZone(ZonedDateTime dateTime) {
        DateTimeFormatter timeFormatter = DateTimeFormatter.ofPattern("hh:mm:ss");
        DateTimeFormatter timeZoneFormatter = DateTimeFormatter.ofPattern("z");

        String time = dateTime.format(timeFormatter);
        String timeZone = dateTime.format(timeZoneFormatter);

        return time + " " + timeZone;
    }

    public static void main(String[] args) {
        ZonedDateTime now = ZonedDateTime.now();
        String formattedTime = getTimeWithTimeZone(now);
        System.out.println("Current Time in hh:mm:ss with Time Zone: " + formattedTime);
    }
}

```


```Java
TimeFormatExample.main(new String[]{})
```

    Current Time in hh:mm:ss with Time Zone: 09:05:16 PDT


## 12)Write a java program to read size n from user and to print the following pattern.
1 3 5 7 9 ……….


```Java
import java.util.Scanner;
public class skiptwo{
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter how many times do you want to skip two: ");
        int choice = scanner.nextInt();
        int seq_start = 1;
        for(int i = 1; i<= choice; i++){
            System.out.print(seq_start);
            System.out.print(" ");
            seq_start++; seq_start++;
        }
    }
}
```


```Java
skiptwo.main(new String[]{})
```

    Enter how many times do you want to skip two: 

     13


    1 3 5 7 9 11 13 15 17 19 21 23 25 

## 13)Write a java program to read size n from user and to print the following pattern.
2 4 6 8 10 ………


```Java
import java.util.Scanner;
public class skiptwoEven{
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter how many times do you want to skip two starting at 2: ");
        int choice = scanner.nextInt();
        int seq_start = 2;
        for(int i = 1; i<= choice; i++){
            System.out.print(seq_start);
            System.out.print(" ");
            seq_start++; seq_start++;
        }
    }
}
```


```Java
skiptwoEven.main(new String[]{})
```

    Enter how many times do you want to skip two starting at 2: 

     13


    2 4 6 8 10 12 14 16 18 20 22 24 26 

## 14)Write a java program to print month name for the given month number


```Java
public class Months{
    public static void MonthNameFromInteger(int monthNumber){

            String monthName;
            switch (monthNumber) {
                case 1:  monthName = "January";   break;
                case 2:  monthName = "February";  break;
                case 3:  monthName = "March";     break;
                case 4:  monthName = "April";     break;
                case 5:  monthName = "May";       break;
                case 6:  monthName = "June";      break;
                case 7:  monthName = "July";      break;
                case 8:  monthName = "August";    break;
                case 9:  monthName = "September"; break;
                case 10: monthName = "October";   break;
                case 11: monthName = "November";  break;
                case 12: monthName = "December";  break;
                default: monthName = "Invalid month number"; break;
            }

            System.out.println("Month: " + monthName);
        } 

    public static void main(String[] args) {
        int monthNumber = Integer.parseInt(args[0]);
        MonthNameFromInteger(monthNumber);
    }
}
```


```Java
Months.MonthNameFromInteger(1)
```

    Month: January


## 15)Write the java program to print age group depending on the age value entered.

    - If age<=2 then age group is toddler  
    - If age>2 and age<=10 then age group is kid  
    - If age>10 and age<=18 then children  
    - If age>18 and age<=30 then young adult  
    - If age>30 and age<=45 then adult  
    - If age>45 then old adult  


```Java
public class categorizeAge{
    public static String getAgeCateg(int age){
        String res;
        if(age <= 2){res = "toddler";}
        else if(age <= 10){res = "kid";}
        else if(age <= 18){res = "children";}
        else if(age <= 30){res = "young adult";}
        else if(age <= 45){res = "adult";}
        else{res = "old adult";}
        return res;
    }
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        String categ = getAgeCateg(age);
        System.out.println("Your age group, at age "+age+", is "+categ);
                    
    }
}
```


```Java
categorizeAge.main(new String[]{})
```

    Enter your age: 

     16


    Your age group, at age 16, is children


## 16)Write a java program to find an element in a array of elements


```Java
public class FindElementInArray {

    // Function to find the index of the element, returns -1 if not found
    public static int findNumIndex(int[] array, int NumToSearch) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == NumToSearch) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java findNumIndex [1, 2, 3, 4] <number_to_search>");
            return;
        }

        String listString = args[0];
        
        // process the array for search
        listString = listString.replace("[", "").replace("]", "").trim();
        String[] nums = listString.split(",");
        int[] array = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            array[i] = Integer.parseInt(nums[i].trim());
        }

        // argument 2 = element to search
        int numToSearch = Integer.parseInt(args[1]);

        // Call the function find the index
        int index = findNumIndex(array, numToSearch);

        // Print Interpretation
        if (index != -1) {
            System.out.println("Element " + numToSearch + " found at index " + index);
        } else {
            System.out.println("Element " + numToSearch + " not found in the array.");
        }
    }
}

```


```Java
FindElementInArray.main(new String[] {"[1,2,3,4,5]", "3"})
```

    Element 3 found at index 2


## 17)Write a java program to find maximum of two num and maximum of 3 numbers using function overloading


```Java
public class MaxNumFinder {

    public static int max(int a, int b) {
        System.out.println("Calculating max of two");
        int res;
        if(a>=b){res=a;}
        else{res=b;}
        return res;
    }

    public static int max(int a, int b, int c) {
        System.out.println("Calculating max of three");
        int res;
        if(a>=b && a>=c){res=a;}
        else if(b>=a && b>=c){res=b;}
        else {res=c;}
        return res;
    }

    public static void main(String[] args) {
        // Test maximum of two numbers
        int maxOfTwo = max(10, 20);
        System.out.println("Maximum of 10 and 20 is: " + maxOfTwo);

        // Test maximum of three numbers
        int maxOfThree = max(15, 30, 25);
        System.out.println("Maximum of 15, 30, and 25 is: " + maxOfThree);
    }
}
```


```Java
MaxNumFinder.max(1,2)
```

    Calculating max of two





    2




```Java
MaxNumFinder.max(1,2,3)
```

    Calculating max of three





    3



## 18)Write a java program to print the sum of a given array elements of size n. (read all the input from user)


```Java
public class sumArray {

    public static int sumArray(int[] array) {
        int sum_all = 0;
        for (int i = 0; i < array.length; i++) {
            sum_all = sum_all+array[i];
            }
        return sum_all;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java sumArray [1, 2, 3, 4]");
            return;
        }

        String listString = args[0];
        
        // process to create array
        listString = listString.replace("[", "").replace("]", "").trim();
        String[] nums = listString.split(",");
        int[] array = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            array[i] = Integer.parseInt(nums[i].trim());
        }

        // Call the function find the index
        int sum_arr = sumArray(array);

        // Print Sum
        System.out.println("Sum of array " + args[0] + " is = " + sum_arr);
    }
}
```


```Java
sumArray.main(new String[] {"[1,2,3]"})
```

    Sum of array [1,2,3] is = 6


## 19)Write a java program to print area of triangle and circle


```Java
import java.util.Scanner;

public class AreaCalculator {
    public static double calcTriangleArea(double base, double height) {
        return 0.5 * base * height;
    }
    public static double calcCircleArea(double radius) {
        return Math.PI * radius * radius;
    }
    public static void getTriangleSpecs(Scanner scanner) {
        System.out.println("Enter triangle base: ");
        double base = scanner.nextDouble();
        System.out.println("Enter triangle height: ");
        double height = scanner.nextDouble();
        
        double area = calcTriangleArea(base, height);
        System.out.println("The area of the triangle is: " + area);
    }

    public static void getCircleSpecs(Scanner scanner) {
        System.out.println("Enter circle radius: ");
        double radius = scanner.nextDouble();
        double area = calcCircleArea(radius);
        System.out.println("The area of the circle is: " + area);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Choose to calculate the area:");
        System.out.println("1. Triangle");
        System.out.println("2. Circle");
        System.out.print("Enter your choice (1 or 2): ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            getTriangleSpecs(scanner);
        } else if (choice == 2) {
            getCircleSpecs(scanner);
        } else {
            System.out.println("Invalid choice! Please enter 1 for Triangle or 2 for Circle.");
        }
        
        scanner.close();
    }
}

```


```Java
AreaCalculator.main(new String[]{})
```

    Choose to calculate the area:
    1. Triangle
    2. Circle
    Enter your choice (1 or 2): 

     
     1


    Enter triangle base: 


     23


    Enter triangle height: 


     34


    The area of the triangle is: 391.0



```Java
AreaCalculator.main(new String[]{})
```

    Choose to calculate the area:
    1. Triangle
    2. Circle
    Enter your choice (1 or 2): 

     2


    Enter circle radius: 


     34


    The area of the circle is: 3631.6811075498013


## 20)Write a java program to Find the even numbers in the given integer array of size n


```Java
public class printEvenFromArray {

    public static void printEvenFromArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            if(array[i]%2==0){
                System.out.print(array[i]+" ");
            }
            }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java printEvenFromArray [1, 2, 3, 4]");
            return;
        }

        String listString = args[0];
        
        // process to create array
        listString = listString.replace("[", "").replace("]", "").trim();
        String[] nums = listString.split(",");
        int[] array = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            array[i] = Integer.parseInt(nums[i].trim());
        }

        // Call the function to print even numbers
        printEvenFromArray(array);
    }
}
```


```Java
printEvenFromArray.main(new String []{"[1,2,3,4,5,6,7,8]"})
```

    2 4 6 8 

## 21)Write a java program to Swap 2 numbers without using the 3rd variable.


```Java
public class nums {
    public static void nums_swap(int a, int b) {
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.print(a+", "+b);
    }
}
```


```Java
nums.nums_swap(2,3)
```

    3, 2

## 22)Write a java program to Find the frequency of the given character in the given string.


```Java
import java.util.Scanner;

public class CharFreq {
    public static int getCharFreq(String in_str, char in_char) {

        // each to_lower
        in_str = in_str.toLowerCase();
        in_char = Character.toLowerCase(in_char);
        
        // Now count
        int freq = 0;
        for (int i = 0; i < in_str.length(); i++) {
            if (in_str.charAt(i) == in_char) {
                freq++;
            }
        }
        return freq;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the string. e.g., This is a great example: ");
        String str = scanner.nextLine();
        
        System.out.print("Enter the character to find its frequency, e.g., e: ");
        char ch = scanner.next().charAt(0);

        int frequency = getCharFreq(str, ch);

        System.out.println("The frequency of '" + ch + "' in the string is: " + frequency);
        
        scanner.close();
    }
}
```


```Java
CharFreq.main(new String[]{})
```

    Enter the string. e.g., This is a great example: 

     exemplify please


    Enter the character to find its frequency, e.g., e: 

     e


    The frequency of 'e' in the string is: 4


## 23)Write a Java program to Accept Name, Age, Gender and Aadhaar number of a person from the user and print them in separate lines


```Java
import java.util.Scanner;
public class GetDetails{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your name: ");
        String name = scanner.nextLine();
        System.out.println("What is your age: ");
        String age = scanner.nextLine();
        System.out.println("What is your Gender: ");
        String gender = scanner.nextLine();
        System.out.println("What is your Adhaar No.: ");
        String aadhar = scanner.nextLine();
        System.out.println("\n\n");
        System.out.println("Details for "+name+":");
        System.out.println("Age: "+age);
        System.out.println("Gender: "+gender);
        System.out.println("Adhaar No.: "+aadhar);
        scanner.close();
        
}}
```


```Java
GetDetails.main(new String[]{})
```

    What is your name: 


     Jas


    What is your age: 


     16


    What is your Gender: 


     Male


    What is your Adhaar No.: 


     1233


    
    
    
    Details for Jas:
    Age: 16
    Gender: Male
    Adhaar No.: 1233


## 24)Write a Java program to Print the area(width\*height) and perimeter(2\*(width+height)) of a rectangle


```Java
public class MyRectangle {
    public static double perimeter(double width, double height) {
        return 2 * width * height;
            }
    public static double area(double width, double height) {
        // there is no r**2 in JAVA!!
        return width * height;
            }
    public static double[] PeriNArea(double width, double height) {
        return new double[] {perimeter(width, height), area(width, height)};
            }
    public static void main(double width, double height) {
        double[] results = PeriNArea(width, height);

        System.out.println("Rectangle Area = "+results[1]);
        System.out.println("Rectangle Perimeter = "+results[0]);
    }
}
```


```Java
MyRectangle.main(3,4)
```

    Rectangle Area = 12.0
    Rectangle Perimeter = 24.0


## 25)Write a Java program to Write java programs to print the following patterns:

    - P1) 
        12345
        12345
        12345
        12345
        12345


```Java
// 25-P1. print the pattern 12345 5 times
public class PatternPrinter{
    public static void printNums(){
        for(int i = 1; i<=5; i++){
            System.out.println("12345");
        }
        return;
    }
}
```


```Java
PatternPrinter.printNums()
```

    12345
    12345
    12345
    12345
    12345


    - P2)
        11111
        22222
        33333
        44444
        55555


```Java
// 25-P2. print the pattern 12345 5 times
public class PatternPrinter{
    public static void printNums(){
        int a = 1111; int res=0;
        for(int i = 1; i<=5; i++){
            res=res+a;
            System.out.println(res);
        }
        return;
    }
}
```


```Java
PatternPrinter.printNums()
```

    1111
    2222
    3333
    4444
    5555


    - P3)
        1
        11
        111
        1111


```Java
// 25-P3. print the pattern 12345 5 times
public class PatternPrinter{
    public static void printNums(){
        int a = 1; int res=0;
        for(int i = 1; i<=4; i++){
            res=res*10+a;
            System.out.println(res);
        }
        return;
    }
}
```


```Java
PatternPrinter.printNums()
```

    1
    11
    111
    1111


    - P4)
        1
        111
        11111
        1111111


```Java
// 25-P5. print the pattern 12345 5 times
public class PatternPrinter{
    public static void printNums(){
        int a = 1; int res=0;
        System.out.println(a);
        for(int i = 1; i<4; i++){
            res=res*10+a;
            res=res*10+a;
            System.out.println(res);
        }
        return;
    }
}
```


```Java
PatternPrinter.printNums()
```

    1
    11
    1111
    111111


    - P5)
        12345
        1234
        123
        12
        1


```Java
// 25-P5. print the pattern 12345 5 times
public class PatternPrinter{
    public static void main(String[] args) {
        int n = 5; // Number of lines in the pattern

        // Outer loop for each line
        for (int i = n; i > 0; i--) {
            // Inner loop to print numbers
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            // Move to the next line after printing all numbers for the current line
            System.out.println();
        }
    }
}
```


```Java
PatternPrinter.main(new String[]{})
```

    12345
    1234
    123
    12
    1



```Java
// 25-P5. Print pattern P5
public class PatternPrint{
    public static void printReducing(){
        
        for(int i = 1; i <= 5; i++){
            String pattern = "";
            for(int j = i; j <= 5; j++){
                pattern = pattern + j;
        }    
        System.out.println(pattern);
        }
    }
}
```


```Java
PatternPrint.printReducing()
```

    12345
    2345
    345
    45
    5


## 26. Swap two number with and without using third variable.


```Java
public class nums {
    //swap using variable
    public static void nums_swap_usevar(int a, int b) {
        int c = a;
        a = b;
        b = c;
        System.out.println(a+" "+b);
    }
    // swap without using a variable
    public static void nums_swap_novar(int a, int b) {
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println(a+" "+b);
    }
}
```


```Java
nums.nums_swap_usevar(4,3)
```

    3 4



```Java
nums.nums_swap_novar(5,3)
```

    3 5


## 27. Write a program to find factorial.(iterative and recursive technique) 


```Java
import java.util.Scanner;
public class factorials{
    public static int recursiveFactorial(int a){
        //base case
        if(a<=1){
            return 1;
                }
        //recursive case
        else {
            return a*recursiveFactorial(a-1);
    }}
    public static int iterativeFactorial(int a){
        int res=1;
        for(int b=a; b>=1; b--){
            res = res*b;
        }
        return res;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number to compute its factorial: ");
        int number = scanner.nextInt();

        int rec_result = recursiveFactorial(number);
        System.out.println("The factorial of " + number + " with recursive code is: " + rec_result);
        
        int itr_result = iterativeFactorial(number);
        System.out.println("The factorial of " + number + " with iterative code is: " + itr_result);
        
        scanner.close();
    }
        
    }
```


```Java
factorials.main(new String[]{})
```

    Enter a number to compute its factorial: 

     23


    The factorial of 23 with recursive code is: 862453760
    The factorial of 23 with iterative code is: 862453760


## 28. Write a program to check whether the given number is prime number or not.


```Java
import java.util.Scanner;

public class PrimeNumberChecker {
    /* To check if a given number is a prime number, 
    we need to determine whether it has any divisors other than 1 and itself. 
    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    */

    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // ~it is not a prime
            }
        }
        return true; // ~it is a prime
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        boolean prime = isPrime(number);

        if (prime) {
            System.out.println(number + " is a prime number.");
        } else {
            System.out.println(number + " is not a prime number.");
        }

        scanner.close();
    }
}
```


```Java
PrimeNumberChecker.main(new String[]{})
```

    Enter a number: 

     23


    23 is a prime number.


## 29. Write a program to-
- prompt the user "you want to reverse a digit or a string ?". 
- according to user input, your program should
    - reverse the digits of the NUMBERS or reverse the string.


```Java
import java.util.Scanner;
public class RevString{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Do you want to reverse a 'number' or a 'string'?: ");
        String inp_type = scanner.nextLine().trim().toLowerCase();
        
        System.out.print("Enter your input: ");
        String inp = scanner.nextLine().trim();

        //reverse it
        String reversedIn = new StringBuilder(inp).reverse().toString();
        System.out.println("Reversed: " + reversedIn);

        scanner.close();
    }
}
```


```Java
RevString.main(new String[]{})
```

    Do you want to reverse a 'number' or a 'string'?: 

     number


    Enter your input: 

     1234567890


    Reversed: 0987654321



```Java
RevString.main(new String[]{})
```

    Do you want to reverse a 'number' or a 'string'?: 

     string


    Enter your input: 

     I am going to reverse this


    Reversed: siht esrever ot gniog ma I


## 29B
- Create the student class with name, university, id, GDP.
- Read number of students and store the student information.
- use constructors. private properties with getters and setters.
- Set university as "tekarch" for all the students. write the functions for the following.

* Read all the student information by name.
* Read all the student information by id.
* print all student information
* update the student GDP using student id

__this one needs a little clarification on what needs to be performed, plus it is put in as a subtask__


```Java
import java.util.ArrayList;
import java.util.Scanner;

class Student{
    private String name;
    private String univ;
    private int id;
    private double gpa; // is gdp = gpa??

    // Constructor to initialize student
    public Student(String name, int id, double gdp){
        this.name = name;
        this.id = id;
        this.gpa = gpa; // what is gdp??
        this.univ = "tekarch"; //the default
    }

    // gets
    public String getName(){
        return name;
    }

    public int getID(){
        return id;
    }

    public double getGPA(){
        return gpa;
    }

    //set
    public void setGPA(double gpa){
        this.gpa = gpa;
    }

    public String getUniv(){
        return univ;
    }

    //print student info
    public void printStuInfo(){
        System.out.println("Name: "+name+" ID:"+id+", University:"+univ+" GPA:"+gpa);

    }}
```


```Java
public class StudentInfo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //scan info
        System.out.println("Enter student's info: ");
        System.out.print("Name: ");
        String name = scanner.nextLine();
        System.out.print("ID: ");
        int id = scanner.nextInt();
        System.out.print("GPA: ");
        double gpa = scanner.nextDouble();

        // Create a Student object
        Student student = new Student(name, id, gpa);

        // Print info
        System.out.println("\nStudent Information:");
        student.printStuInfo();

        scanner.close();
    }
}
        
        
```


```Java
StudentInfo.main(new String[]{})
```

    Enter student's info: 
    Name: 

     Jas


    ID: 

     1233


    GPA: 

     3.83


    
    Student Information:
    Name: Jas ID:1233, University:tekarch GPA:0.0


## 30. write a java program to find the given year a leap year or not.


```Java
import java.util.Scanner;

public class LeapYearChecker {
    public static boolean isLeapYear(int year) {
        if (year % 400 == 0) {
            return true; 
        } else if (year % 100 == 0) {
            return false; 
        } else if (year % 4 == 0) {
            return true; 
        } else {
            return false; 
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a year: ");
        int year = scanner.nextInt();

        // Check if the year is a leap year
        boolean leapYear = isLeapYear(year);

        if (leapYear) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }

        scanner.close();
    }
}
```


```Java
LeapYearChecker.main(new String[]{})
```

    Enter a year: 

     2024


    2024 is a leap year.

