public class Temp{
    public static void main(String[] args) {
       int n = 16;
       int ans = isHappy(n);

       if(ans == 1){
            System.out.println("Happy");
       }
       else{
            System.out.println("not");
       }

    }
    public static int isHappy(int n){
        while(n != 1 && n != 4){
            int sum = 0;

            while(n > 0){
                int d = n%10;
                sum += d*d;
                n = n/10;
            }
            
            n = sum;
        }
        if(n == 1) return 1;
        return 0;
    }
}