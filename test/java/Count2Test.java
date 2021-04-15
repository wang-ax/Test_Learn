import org.junit.Ignore;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-14
 * Time 20:18
 */
public class Count2Test {
    //验证超时
    @Test(timeout = 100)
    public void testAdd() throws InterruptedException {
        Thread.sleep(101);
        new Count2().add(1,1);
    }

    //验证抛出异常
    @Test(expected = ArithmeticException.class)
    public void  testDivision(){
        new Count2().division(8,0);
    }

    //跳过该条测试用例
    @Ignore//用来标识该用例提跳过
    @Test//表示是一条测试用例
    public void testAdd2(){
        Count2 count2 = new Count2();
        int result = count2.add(2,2);
        assertEquals(result,5);
    }
}
