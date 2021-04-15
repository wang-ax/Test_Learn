import org.junit.*;

import static org.junit.Assert.assertEquals;

/**
 * ClassName PACKAGE_NAME
 * Description TODO
 * Author 30712
 * Date 2021-04-14
 * Time 21:24
 */

/**
 * 如果是 web UI自动化测试，可以把浏览器驱动的定义放到@Before中，浏览器的关闭放到@After中
 *
 */
public class TestFixture {
    //在当前的测试类开始之前执行
    @BeforeClass
    public static  void  beforeClass(){
        System.out.println("----------beforeClass");
    }
    //在当前测试类结束时运行
    @AfterClass
    public static void  afterClass(){
        System.out.println("-----------afterClass");
    }

    //在每一个测试方法之前运行
    @Before
    public void before(){
        System.out.println("=======before");
    }

    //在每一个测试方法之后运行
    @After
    public void after(){
        System.out.println("=========after");
    }


    @Test
    public void testAdd1(){
        int result = new Count().add(5,3);
        assertEquals(result,8);
        System.out.println("test Run testAdd1");
    }

    @Test
    public void testAdd2(){
        int result = new Count().add(15,13);
        assertEquals(result,28);
        System.out.println("test Run testAdd2");
    }
}
