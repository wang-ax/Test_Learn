import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-14
 * Time 20:11
 */
public class CountTest {//测试已经写好的功能模块Count
    @Test
    public  void testAdd(){
        Count count = new Count();
        int result = count.add(2,2);
        assertEquals(result,4);//用于判断两个值是否相关
    }
}
