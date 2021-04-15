/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-14
 * Time 21:39
 */
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;
import static org.junit.Assert.assertEquals;

// 按字母顺序执行
@FixMethodOrder(MethodSorters.NAME_ASCENDING)//用例的执行顺序
public class TestRunSequence {

    @Test
    public void TestCase1() {
        assertEquals(2+2, 4);
    }

    @Test
    public void TestCase2() {
        assertEquals(2+2, 4);
    }

    @Test
    public void TestAa() {
        assertEquals("hello", "hello");
    }
}