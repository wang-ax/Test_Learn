import org.junit.Test;

import static org.junit.Assert.assertTrue;

/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-14
 * Time 21:50
 */
public class AssertTest {
    @Test
    public  void testPrime(){
        int n =7;
        Prime prime  = new Prime();
        assertTrue(prime.Prime(n));
    }
}
