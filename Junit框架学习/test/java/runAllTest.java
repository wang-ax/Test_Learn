import org.junit.runner.RunWith;
import org.junit.runners.Suite;

/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-15
 * Time 21:45
 */
@RunWith(Suite.class)
@Suite.SuiteClasses({
        CountTest.class,
        TestFixture.class,
        AssertTest.class,
        TestRunSequence.class,
})
//要创建一个空的类，作为测试套件的入口
public class runAllTest {

}
