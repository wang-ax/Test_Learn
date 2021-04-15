/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-14
 * Time 21:50
 */
public class Prime {
    //判断一个数是否为素数
    public   Boolean Prime(int n){
        for (int i=2;i< Math.sqrt(n);i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }
}
