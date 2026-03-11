# Examen 1Z0-829 - Java SE 17 Developer
## Simuladores Preguntas y Respuestas

> Nota: El examen tiene 50 paginas pero las preguntas 47 y 48 no existen.

---

### Pregunta 1 (Page 1 of 50)
**Given the content of the `in.txt` file:**
```
0123456789
```

**and the code fragment:**
```java
char[] buffer = new char[8];
int count = 0;
try(FileReader in = new FileReader("in.txt");
    FileWriter out = new FileWriter("out.txt")) {
    while((count = in.read(buffer)) != -1) {
        out.write(buffer);
    }
}
```

**What is the content of the `out.txt` file?**

- A) 01234567801234
- B) 01234567
- C) 012345678
- D) 012345678901234
- E) 0123456789
- F) 012345678923456789

---

### Pregunta 2 (Page 2 of 50)
**Given the code fragment:**
```java
// line n1
String input = console.readLine("Input a number: ");
int number = Integer.parseInt(input);

if (number % 2 == 0) {
    System.out.println(number + " is even.");
} else {
    System.out.println(number + " is odd");
}
```

**Which code at `line n1` obtains the `java.io.Console` object?**

- A) `Console console = new Console(new InputStreamReader(System.in));`
- B) `Console console = System.console(System.in);`
- C) `Console console = Console.getInstance();`
- D) `Console console = System.console();`
- E) `Console console = new Console(System.in);`

---

### Pregunta 3 (Page 3 of 50)
**Given:**
```java
class Product {
    String name; double price;
    Product(String s, double d) {
        this.name = s;
        this.price = d;
    }
}
class ElectricProduct extends Product {
    ElectricProduct(String name, double price) {
        super(name, price);
    }
}
```

**and the code fragment:**
```java
List<Product> p = List.of(
    new ElectricProduct("CellPhone",100),
    new ElectricProduct("ToyCar",90),
    new ElectricProduct("Motor",200),
    new ElectricProduct("Fan",300)
);

DoubleSummaryStatistics sts = p.stream().filter(a -> a instanceof ElectricProduct)
                                .collect(Collectors.summarizingDouble(a -> a.price));
String s1 = p.stream().filter(a -> a instanceof Product)
              .collect(Collectors.mapping(p2 -> p2.name, Collectors.joining(",")));
System.out.println(sts.getMax());
System.out.println(s1);
```

**What is the result?**

- A) 100.00 / CellPhone,ToyCar
- B) 100.00 / CellPhone,ToyCar,Motor,Fan
- C) 300.00 / CellPhone,ToyCar,Motor,Fan- D) 300.00 / CellPhone,ToyCar

---

### Pregunta 4 (Page 4 of 50)
**Given the code fragment:**
```java
List<String> specialDays = List.of("NewYear","Valentines","Spring","Labour");
System.out.print(specialDays.stream().allMatch(s ->s.equals("Labour")));
System.out.print(" " + specialDays.stream().anyMatch(s ->s.equals("Labour")));
System.out.print(" " + specialDays.stream().noneMatch(s -> s.equals("Halloween")));
System.out.print(" " +specialDays.stream().findFirst());
```

**What is the result?**

- A) `0 1 1 0`
- B) `true true false NewYear`
- C) `0 1 0 Optional[NewYear]`
- D) `false true true Optional[NewYear]`
---

### Pregunta 5 (Page 5 of 50)
**Given the code fragment:**
```java
List lst = new ArrayList();
lst.add("e1");
lst.add("e3");
lst.add("e2");

int x1 = Collections.binarySearch(lst, "e3");
System.out.println(x1);
Collections.sort(lst);
int x2 = Collections.binarySearch(lst, "e3");
System.out.println(x2);

Collections.reverse(lst);
int x3 = Collections.binarySearch(lst, "e3");
System.out.println(x3);
```

**What is the result?**

- A) 1 / 1 / 1
- B) 1 / 2 / -4
- C) 0 / 2 / -2
- D) 2 / 2 / 0

---

### Pregunta 6 (Page 6 of 50)
**Given the code fragment:**
```java
class Book {
    String author;
    String title;
    Book(String authorName, String title) {
        this.author = authorName;
        this.title = title;
    }
}

class SortBook {
    public static void main(String[] args) {
        List books = List.of(new Book("A1","T1"), new Book("A2", "T2"), new Book("A1","T2")); // Line n1
        books.sort((Book a, Book b) -> a.title.compareTo(b.title));    // Line n2
        System.out.println(books);
    }
}
```

**Which action sorts the book list?**

- A) At Line n1, convert `books` type to mutable `ArrayList` type.
- B) At Line n2, replace `compareTo()` with `compare()`.
- C) At Line n2, replace `books.sort()` with `books.stream().sort()`.
- D) At Line n1, convert `books` type to mutable array type.

---

### Pregunta 7 (Page 7 of 50)
**Given the code fragment:**
```java
Stream<String> s1 = Stream.of("A", "B", "C", "B");
Stream<String> s2 = Stream.of("A", "D", "E");
Stream.concat(s1, s2).parallel().distinct().forEach(element -> System.out.print(element));
```

**What is the result?**

- A) `ABCDE` // the order of elements is unpredictable
- B) `ADEABCB` // the order of elements is unpredictable
- C) `ABCDE`
- D) `ABBCDE` // the order of elements is unpredictable

---

### Pregunta 8 (Page 8 of 50)
**Given:**
```java
public class Test {
    public static void main(String[] args) {
        List<String> elements =
            Arrays.asList("car", "truck", "car",
                          "bicycle", "car", "truck", "motorcycle");
        Map<String, Long> outcome =
            elements.stream().collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        System.out.println(outcome);
    }
}
```

**What is the result?**

- A) `{bicycle=7, car=7, motorcycle=7, truck=7}`
- B) `{3:bicycle, 0:car, 6:motorcycle, 5:truck}`
- C) Compilation fails.
- D) `{bicycle=1, car=3, motorcycle=1, truck=2}`
- E) `{bicycle, car, motorcycle, truck}`

---

### Pregunta 9 (Page 9 of 50)
**Given:**
```java
public class Test {
    public String attach1(List<String> data) {
        return data.parallelStream().reduce("w", (n,m) -> n+m, String::concat);
    }
    public String attach2(List<String> data) {
        return data.parallelStream().reduce((l, p)-> l+p).get();
    }

    public static void main(String[] args) {
        Test t = new Test();
        var list = List.of("Table", "Chair");
        String x = t.attach1(list);
        String y = t.attach2(list);
        System.out.print(x+ " "+y);
    }
}
```

**What is the result?**

- A) Compilation fails.
- B) TableChair TableChair
- C) A `RuntimeException` is thrown.
- D) wTablewChair TableChair
- E) wTableChair TableChair

---

### Pregunta 10 (Page 10 of 50)
**Given the code fragment:**
```java
Pet p = new Pet("Dog");
Pet p1 = p;
p1.name = "Cat";
p = p1;
System.out.println(p.name);
p = null;
System.out.println(p1.name);
```

**What is the result?**

- A) A `NullPointerException` is thrown.
- B) Dog / Dog
- C) Cat / Dog
- D) Cat / null
- E) Cat / Cat *
---

### Pregunta 11 (Page 11 of 50)
**Given:**
```java
public class App{
    String name;
    public App(String name){
        this.name = name;
    }
    public static void main(String args[]) {
        App t1= new App("t1");
        App t2= new App("t2");
        t1 = t2;
        t1 = null;
        System.out.println("GC");
    }
}
```

**Which statement is true while the program prints `GC`?**

- A) Only one of the objects previously referenced by `t1` is eligible for garbage collection.
- B) Only the object referenced by `t2` is eligible for garbage collection.
- C) Both the objects previously referenced by `t1` are eligible for garbage collection.
- D) None of the objects are eligible for garbage collection.

---

### Pregunta 12 (Page 12 of 50)
**Assuming that the `data.txt` file exists and has the following content:**
```
text1
text2
text3
```

**Given the code fragment:**
```java
try {
    Path p = new File("data.txt").toPath();
    Stream lines = Files.lines(p);
    String data = lines.collect(Collectors.joining("-"));
    System.out.println(data);
    String data2 = Files.readAllLines(p).get(3);
    System.out.println(data2);
} catch (IOException ex) {
    System.out.println(ex);
}
```

**What is the result?**

- A) text1-text2-text3 / text3
- B) text1-text2-text3 / A `java.lang.IndexOutOfBoundsException` is thrown.
- C) text1- / text2- / text3- / text3
- D) text1-text2-text3 / text1 / text2 / text3

---

### Pregunta 13 (Page 13 of 50)
**Given the code fragment:**
```java
record Product(int pNumber, String pName) {
    int regNo = 100;
    public int getRegNumber() {
        return regNo;
    }
}

public class App {
    public static void main(String[] args) {
        Product p1 = new Product(1111, "Ink Bottle");
    }
}
```

**Which action enables the code to compile?**

- A) Make the `regNo` variable `static`.
- B) Replace `record` with `void`. 
- C) Make the `regNo` variable `public`.
- D) Replace `record` with `class`. 
- E) Remove the `regNo` initialization statement.

---

### Pregunta 14 (Page 14 of 50)
**Given:**
```java
1. class Item {
2.     String name;
3.     public static void display() {
4.         name = "Vase"; //Don't Compile
5.         System.out.println(name);
6.     }
7.     public void display(String design) {
8.         this.name += name;
9.         System.out.println(name);
10.    }
11. }
12. public class App {
13.     public static void main(String[] args) {
14.         Item i1 = new Item();
15.         i1.display("Flower");
16.     }
17. }
```

**Which action enables the code to compile?**

- A) Replace 7 with `public static void display(String design) {`
- B) Replace 2 with `static String name;` 
- C) Replace 3 with `private static void display() {`
- D) Replace 15 with `Item.display("Flower");`

---

### Pregunta 15 (Page 15 of 50)
**Given the course table:**

| COURSE_ID | COURSE_NAME | COURSE_FEE | COURSE_LEVEL |
|-----------|-------------|------------|--------------|
| 1021 | Java Programmer | 400.00 | 1 |
| 1022 | Java Architect | 600.00 | 2 |
| 1023 | Java Master | 600.00 | 2 |

**Given the code fragment:**
```java
try (Connection con = DriverManager.getConnection(connectionString)) {
    Statement statement = con.createStatement(TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_UPDATABLE);
    String qry = "UPDATE course SET course_fee = ? where COURSE_LEVEL = ?";
    PreparedStatement prStmt = con.prepareStatement(qry, TYPE_SCROLL_INSENSITIVE);
    prStmt.setDouble(1,600.00);
    prStmt.setInt(2,2);
    System.out.println(prStmt.executeUpdate());
}
catch(SQLException sqlException) {
    System.out.println(sqlException);
}
```

**What is the result?**

- A) 2
- B) false
- C) 1
- D) true

---

### Pregunta 16 (Page 16 of 50)
**Given the code fragment:**
```java
String s = "10_00";
Integer s2 = 10_00;
// Line n1
System.out.println(res);
```

**Which two statements at `Line n1` independently enable you to print `1250`?**

- A) `Integer res = 250 + Integer(s2);` 
- B) `Integer res = 250;` / `res += s2;` 
- C) `Integer res = 250 + s;` 
- D) `Integer res = 250 + Integer.valueOf(s);`
- E) `Integer res = 250 + Integer.parseInt(s);` 
- F) `Integer res = 250 + s2;` 

---

### Pregunta 17 (Page 17 of 50)
**Given the code fragment:**
```java
int a = 2;
int b = ~a; -3
int c = a^b; -1
boolean d = a < b & a > c++;
System.out.println(d + " " + c);
boolean e = a > b && a > c++;
System.out.println(e + " " + c);
```

**What is the result?**

- A) false 1 / true 2
- B) true 1 / false 2
- C) false 1 / false 2
- D) false 0 / true 1 *
---

### Pregunta 18 (Page 18 of 50)
**Given:**
```java
class StockException extends Exception {
    public StockException(String s) { super(s); }
}
class OutofStockException extends StockException {
    public OutofStockException(String s) { super(s); }
}
```

**and the code fragment:**
```java
public class Test {
    public static void main(String[] args) throws OutofStockException {
        m();
    }
    public static void m() throws OutofStockException {
        try {
            throw new StockException("Raised.");
        } catch (Exception e) {
            throw new OutofStockException(e.getMessage());
        }
    }
}
```

**Which statement is true?**

- A) The program throws `StockException`.
- B) The program throws `OutofStockException`. 
- C) The program throws `ClassCastException`.
- D) The program fails to compile.

---

### Pregunta 19 (Page 19 of 50)
**Given:**
```java
final class Folder {    // line n1
    // line n2
    public void open(){
        System.out.print("Open ");
    }
}

public class Test {
    public static void main(String[] args) throws Exception {
        try (Folder f = new Folder()) {
            f.open();
        }
    }
}
```

**Which two modifications enable the code to print `Open Close`?**

- A) At line n2, insert: `public void close() throws IOException { System.out.print("Close "); }` 
- B) At line n2, insert: `final void close() { System.out.print("Close "); }`
- C) Replace line n1 with: `class Folder extends Closeable {`
- D) Replace line n1 with: `class Folder implements AutoCloseable {`
- E) Replace line n1 with: `class Folder extends Exception {`

---

### Pregunta 20 (Page 20 of 50)
**Given:**
```java
class A {public void mA() {System.out.println("mA");}}
class B extends A {public void mB() {System.out.println("mB");}}
class C extends B {public void mC() {System.out.println("mC");}}

public class App {
    public static void main(String[] args) {
        A bobj = new B();
        A cobj = new C();
        if (cobj instanceof B v) {
            v.mB();
            if (v instanceof C v1) { v1.mC(); }
        } else {
            cobj.mA();
        }
    }
}
```

**What is the result?**

- A) mA
- B) mB
- C) mB / mA
- D) mB / mC *

---

### Pregunta 21 (Page 21 of 50)
**Given the directory structure:**
```
module1:
    p1\
        Doc.java
    p2\
        Util.java
```

**Given the definition of the `Doc` class:**
```java
package p1;
public sealed class Doc permits WordDoc {
}
```

**Which two are valid definitions of the `WordDoc` class?**

- A) `package p1;` / `public final class WordDoc extends Doc {}`
- B) `package p1.p2;` / `public non-sealed class WordDoc extends Doc { }`
- C) `package p1;` / `non-sealed abstract class WordDoc extends Doc {}`
- D) `package p1;` / `public non-sealed class WordDoc extends Doc {}`
- E) `package p1.p2;` / `public sealed class WordDoc extends Doc { }`
- F) `package p1;` / `public class WordDoc extends Doc {}`

---

### Pregunta 22 (Page 22 of 50)
**Given:**
```java
public class Test {
    public void sum(int a, int b) {
        System.out.print(" A");
    }
    public void sum(int a, float b) {
        System.out.print(" B");
    }
    public void sum(float a, float b) {
        System.out.print(" C");
    }
    public void sum(double... a) {
        System.out.print(" D");
    }
    public static void main(String[] args) {
        Test t = new Test();
        t.sum(10,15.25);
        t.sum(10, 24);
        t.sum(10.25,10.25);
    }
}
```

**What is the result?**

- A) B A D
- B) D D D
- C) D A D
- D) B A C

---

### Pregunta 23 (Page 23 of 50)
**Given:**
```java
public class Main {
    void print(int i){
        System.out.println("hello");
    }
    void print(long j){
        System.out.println("there");
    }

    public static void main(String[] args) {
        new Main().print(0b1101_1010);
    }
}
```

**What is the result?**

- A) there
- B) Compilation fails.
- C) A `NumberFormatException` is thrown.
- D) hello

---

### Pregunta 24 (Page 24 of 50)
**Given:**
```java
public class Test {
    static interface Animal {
    }
    static class Dog implements Animal {
    }
    private static void play(Animal a) {
        System.out.print("flips");
    }
    private static void play(Dog d) {
        System.out.print("runs");
    }
    public static void main(String[] args) {
        Animal a1 = new Dog();
        Dog a2 = new Dog();
        play(a1);
        play(a2);
    }
}
```

**What is the result?**

- A) runsruns
- B) Compilation fails.
- C) flipsflips
- D) flipsruns
- E) runsflips

---

### Pregunta 25 (Page 25 of 50)
**Given:**

Captions.properties file: `user = UserName`
Captions_en.properties file: `user = User name (EN)`
Captions_US.properties file: `message = User name (US)`
Captions_en_US.properties file: `message = User name (EN - US)`

**and the code fragment:**
```java
Locale.setDefault(Locale.US);
Locale currentLocale = new Locale.Builder().setLanguage("en").build();

ResourceBundle captions = ResourceBundle.getBundle("Captions.properties", currentLocale);
System.out.println(captions.getString("user"));
```

**What is the result?**

- A) User name (US)
- B) User name (EN)
- C) User name (EN - US)
- D) UserName
- E) The program throws a `MissingResourceException`.

---

### Pregunta 26 (Page 26 of 50)
**Given:**
```java
public enum Desig {
    CEO('A'), CMO('B'), CTO('C'), CFO('D');
    char c;
    private Desig(char c) {
        this.c = c;
    }
}
```

**and the code fragment:**
```java
Arrays.stream(Desig.values()).dropWhile(s -> s.equals(Desig.CMO));
switch (Desig.valueOf("CMO")) {
    case CEO -> System.out.println("Executive");
    case CMO -> System.out.println("Marketing");
    case CFO -> System.out.println("Finance");
    case CTO -> System.out.println("Technical");
    default -> System.out.println("UnDefined");
}
```

**What is the result?**

- A) Marketing / Finance / Technical
- B) Marketing / UnDefined
- C) Marketing
- D) UnDefined

---

### Pregunta 27 (Page 27 of 50)
**Given:**
```java
public class Weather {
    public enum Forecast {
        SUNNY, CLOUDY, RAINY;
        @Override
        public String toString() { return "SNOWY";}
    }

    public static void main(String[] args) {
        System.out.print(Forecast.SUNNY.ordinal() + " ");
        System.out.print(Forecast.valueOf("cloudy".toUpperCase()));
    }
}
```

**What is the result?**

- A) Compilation fails
- B) 0 SNOWY
- C) 1 SNOWY
- D) 0 CLOUDY
- E) 1 RAINY

---

### Pregunta 28 (Page 28 of 50)
**Given the code fragment:**
```java
List<Integer> listOfNumbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10); 
```

**Which code fragment returns different values?**

- A) `int sum = listOfNumbers.stream().reduce(0, Integer::sum) + 5;`
- B) `int sum = listOfNumbers.parallelStream().reduce((m, n) -> m + n).orElse(5) + 5;`
- C) `int sum = listOfNumbers.parallelStream().reduce(0, Integer::sum) + 5;`
- D) `int sum = listOfNumbers.parallelStream().reduce(5, Integer::sum);`
- E) `int sum = listOfNumbers.stream().reduce(5, (a, b) -> a+ b);`

---

### Pregunta 29 (Page 29 of 50)
**Given the code fragments:**
```java
class Test {
    volatile int x = 1;
    AtomicInteger xObj = new AtomicInteger(1);
}

public static void main(String[] args) {
    Test t = new Test();
    Runnable r1 = () -> {
        Thread trd = Thread.currentThread();
        while (t.x < 3) {
            System.out.print(trd.getName()+" : "+t.x+" : ");
            t.x++;
        }
    };
    Runnable r2 = () -> {
        Thread trd = Thread.currentThread();
        while (t.xObj.get() < 3) {
            System.out.print(trd.getName()+" : "+t.xObj.get()+" : ");
            t.xObj.getAndIncrement();
        }
    };
    Thread t1 = new Thread(r1,"t1");
    Thread t2 = new Thread(r2,"t2");
    t1.start();
    t2.start();
}
```

**Which is true?**

- A) The program prints an exception.
- B) The program prints `t1 : 1 : t2 : 1 : t1 : 2 : t2 : 2 :` in random order.
- C) The program prints `t1 : 1 : t2 : 1 : t1 : 1 : t2 : 1 :` indefinitely.
- D) The program prints `t1 : 1 : t2 : 1 : t1 : 2 : t2 : 2 :`

---

### Pregunta 30 (Page 30 of 50)
**Which statement is true?**

- A) After the timed wait expires, the waited thread moves to the terminated state.
- B) `IllegalStateException` is thrown if a thread in waiting state is moved back to runnable.
- C) A thread in waiting state consumes CPU cycles.
- D) A thread in waiting state must handle `InterruptedException`.

---






### Pregunta 31 (Page 31 of 50)
**Given the code fragment:**
```java
ExecutorService executorService = Executors.newSingleThreadExecutor();
Set<Callable<String>> workers = new HashSet<Callable<String>>();
workers.add(new Callable<String>() {
    public String call() throws Exception {
        return "1";
    }
});
workers.add(new Callable<String>() {
    public String call() throws Exception {
        return "2";
    }
});
workers.add(new Callable<String>() {
    public String call() throws Exception {
        return "3";
    }
});
```

**Which code fragment invokes all callable objects in the workers set?**

- A) `executorService.submit(cThreads);`
- B) ```java
List<Future<String>> futures = executorService.invokeAny(workers);
for(Future<String> future : futures){
    System.out.println(future.get());
}
```
- C) ```java
for (int i=0; i<3;i++) {
    String result = executorService.invokeAny(cThreads);
    System.out.println(result);
}
```- D) ```java
List<Future<String>> futures = executorService.invokeAll(workers);
for(Future<String> future : futures){
    System.out.println(future.get());
}
```

---

### Pregunta 32 (Page 32 of 50)
**Given the code fragment:**
```java
Integer rank = 4;
switch (rank) {
    case 1,4 -> System.out.println("Range1");
    case 5,8 -> System.out.println("Range2");
    case 9,10 -> System.out.println("Range3");
    default -> System.out.println("Not a valid rank.");
}
```

**What is the result?**

- A) Range1 / Not a valid rank.
- B) Range1 / Range2 / Range3 / Range1 / Not a valid rank.
- C) Range1- D) Range1 / Range2 / Range3

---

### Pregunta 33 (Page 33 of 50)
**Given:**
```java
public class Test {
    public static void main(String[] args) {
        final int x = 2;
        int y = x;
        while (y<3) {
            switch (y) {
                case 0+x:
                    y++;
                case 1:
                    y++;
            }
        }
        System.out.println(y);
    }
}
```

**What is the result?**

- A) Compilation fails.
- B) A runtime exception is thrown.
- C) 6
- D) 4- E) 5
- F) Nothing is printed because of an indefinite loop.
- G) 3
- H) 2

---

### Pregunta 34 (Page 34 of 50)
**Which statement is true about modules?**

- A) Automatic and unnamed modules are on the module path.
- B) Only automatic modules are on the module path.
- C) Automatic and named modules are on the module path.
- D) Only unnamed modules are on the module path.
- E) Only named modules are on the module path.

---

### Pregunta 35 (Page 35 of 50)
**Given:**
```java
package com.transport.vehicle.cars;

public interface Car {
    int getSpeed();
}
```

**and:**
```java
package com.transport.vehicle.cars.impl;

import com.transport.vehicle.cars.Car;

public class CarImpl implements Car {
    private int speed;
    public CarImpl() {
        this(10);
    }
    public CarImpl (int speed) {
        this.speed = speed;
    }
    @Override
    public int getSpeed() {
        return speed;
    }
}
```

**Which two should the `module-info` file include for it to represent the service provider interface?**

- A) `provides com.transport.vehicle.cars.impl.CarImpl to com.transport.vehicle.cars.Car;`
- B) `requires com.transport.vehicle.cars;`
- C) `provides com.transport.vehicle.cars.Car with com.transport.vehicle.cars.impl.CarImpl;`- D) `exports com.transport.vehicle.cars;`
- E) `requires com.transport.vehicle.cars.Car;`
- F) `exports com.transport.vehicle;`
- G) `exports com.transport.vehicle.cars.Car;`

---

### Pregunta 36 (Page 36 of 50)
**Given the code fragment:**
```java
String myStr = "Hello Java 17";
String myTextBlk1 = """
                Hello Java 17""";
String myTextBlk2 = """
                Hello Java 17
                """;
System.out.print(myStr.equals(myTextBlk1)+":");
System.out.print(myStr.equals(myTextBlk2)+":");
System.out.print(myTextBlk1.equals(myTextBlk2)+":");
System.out.println(myTextBlk1.intern() == myTextBlk2.intern());
```

**What is the result?**

- A) true:false:true:false
- B) true:false:false:false- C) true:false:true:true
- D) true:true:false:false

---

### Pregunta 37 (Page 37 of 50)
**Given the code fragment:**
```java
String a = "Hello! Java";
System.out.print(a.indexOf("Java"));
a.replace("Hello!", "Welcome!");
System.out.print(a.indexOf("Java"));
StringBuilder b = new StringBuilder(a);
System.out.print(b.indexOf("Java"));
```

**What is the result?**

- A) 71010
- B) 8109
- C) 777
- D) 7107
- E) 888
- F) 81111

---

### Pregunta 38 (Page 38 of 50)
**Given the code fragment:**
```java
Duration duration = Duration.ofMillis(5000);
System.out.print(duration);
duration = Duration.ofSeconds(60);
System.out.print(duration);
Period period = Period.ofDays(6);
System.out.print(period);
```

**What is the result?**

- A) 5000S60M6D
- B) PT5SPT1MP6D- C) PT5000SPT60MP6D
- D) 5S1M6D

---

### Pregunta 39 (Page 39 of 50)
**Daylight Saving Time (DST) is the practice of advancing clocks at the start of spring by one hour and adjusting them backward by one hour in autumn. Considering that in 2021, DST in Chicago (Illinois) ended on November 7th at 2 AM, and given the fragment:**

```java
ZoneId zoneID = ZoneId.of("America/Chicago");
ZonedDateTime zdt = ZonedDateTime.of(
    LocalDate.of(2021, 11, 7),
    LocalTime.of(1, 30),
    zoneID
);
ZonedDateTime anHourLater = zdt.plusHours(1);
System.out.println(zdt.getHour() == anHourLater.getHour());
System.out.print(zdt.getOffset().equals(anHourLater.getOffset()));
```

**What is the output?**

- A) true / true
- B) true / false
- C) false / true
- D) false / false

---

### Pregunta 40 (Page 40 of 50)
**Given the code fragment:**
```java
// Login time:2021-01-12T21:58:18.817Z
Instant loginTime = Instant.now();
Thread.sleep(1000);

// Logout time:2021-01-12T21:58:19.880Z
Instant logoutTime = Instant.now();

loginTime = loginTime.truncatedTo(ChronoUnit.MINUTES);    // line n1
logoutTime = logoutTime.truncatedTo(ChronoUnit.MINUTES);

if (logoutTime.isAfter(loginTime))
    System.out.println("Logged out at: " + logoutTime);
else
    System.out.println("Can't logout");
```

**What is the result?**

- A) A compilation error occurs at `line n1`.
- B) Can't logout
- C) Logged out at: 2021-01-12T21:58:19.880Z
- D) Logged out at: 2021-01-12T21:58:00Z

---

### Pregunta 41 (Page 41 of 50)
**Which statement is true?**

- A) The `tryLock()` method returns a boolean indicator immediately regardless if it has or has not managed to acquire the lock.
- B) The `lock()` method returns a boolean indicator immediately if it has managed to acquire the lock, otherwise it waits for the lock acquisition.
- C) The `lock()` method returns a boolean indicator immediately regardless if it has or has not managed to acquire the lock.
- D) The `tryLock()` method returns a boolean indicator immediately if it has managed to acquire the lock, otherwise it waits for the lock acquisition.

---

### Pregunta 42 (Page 42 of 50)
**Given the `Product` class:**
```java
import java.io.*;
public class Product implements Serializable {
    private static float averagePrice = 2.99f;
    private String description;
    private transient float price;
    public Product(String description, float price) {
        this.description = description;
        this.price = price;
    }
    public void readObject(ObjectInputStream in)
            throws IOException, ClassNotFoundException {
        in.defaultReadObject();
        price = averagePrice;
    }
    public String toString() {
        return description+" "+price+" "+averagePrice;
    }
}
```

**and the `Shop` class:**
```java
import java.io.*;
public class Shop {
    public static void main(String[] args) {
        Product p = new Product("Cookie", 3.99f);
        try {
            try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("p.ser"))) {
                out.writeObject(p);
            }
            try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("p.ser"))) {
                p = (Product)in.readObject();
            }
        } catch (Exception e) { e.printStackTrace(); }
        System.out.println(p);
    }
}
```

**What is the result?**

- A) Cookie 0.0 2.99
- B) Compilation fails.
- C) Cookie 2.99 2.99
- D) An exception is produced at runtime.
- E) Cookie 0.0 0.0
- F) Cookie 3.99 2.99

---

### Pregunta 43 (Page 43 of 50)
**Given:**
```java
import java.io.Serializable;
public class Software implements Serializable {
    private String title;
    public Software(String title) {
        this.title = title;
        System.out.print("Software ");
    }
    public String toString() { return title; }
}

public class Game extends Software {
    private int players;
    public Game(String title, int players) {
        super(title);
        this.players = players;
        System.out.print("Game ");
    }
    public String toString() { return super.toString()+" "+players; }
}

import java.io.*;
public class AppStore {
    public static void main(String[] args) {
        Software s = new Game("Chess", 2);
        try(ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("game.ser"))) {
            out.writeObject(s);
        } catch (Exception e) {
            System.out.println("write error");
        }
        try(ObjectInputStream in = new ObjectInputStream(new FileInputStream("game.ser"))) {
            s = (Software)in.readObject();
        } catch (Exception e) {
            System.out.println("read error");
        }
        System.out.println(s);
    }
}
```

**What is the result?**

- A) Software Game write error
- B) Software Game Chess 0
- C) Software Game read error
- D) Software Game Software Game Chess 0
- E) Software Game Chess 2
- F) Software Game Software Game Chess 2

---

### Pregunta 44 (Page 44 of 50)
**Given the code fragments:**
```java
class Car implements Serializable {
    private static long serialVersionUID = 454L;
    String name;
    public Car(String name) { this.name = name; }
}

class LuxuryCar extends Car {      // line n1
    int flag_HHC;
    public LuxuryCar(String name, int flag_HHC) {
        super(name);
        this.flag_HHC = flag_HHC;
    }
    public String toString() {
        return name + " : " + flag_HHC;
    }
}
```

**and:**
```java
public static void main(String[] args) {    // line n2
    Car b = new LuxuryCar("Wagon", 200);
    try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("car.ser"));
         ObjectInputStream ois = new ObjectInputStream(new FileInputStream("car.ser"));) {
        oos.writeObject(b);
        System.out.println((Car)(ois.readObject()));        // line n3
    }
}
```

**Which action prints `Wagon : 200`?**

- A) At line n2, in the main method signature, add throws `IOException`, `ClassCastException`.
- B) At line n3, replace `readObject()` with `readLine()`.
- C) At line n1, implement the `java.io.Serializable` interface.
- D) At line n3, replace `Car` with `LuxuryCar`.
- E) At line n1, implement the `java.io.AutoCloseable` interface.
- F) At line n2, in the main method signature, add throws `IOException`, `ClassNotFoundException`.

---

### Pregunta 45 (Page 45 of 50)
**Given the code fragment:**
```java
abstract sealed interface SInt permits Story, Art {
    default String getTitle() { return "Book Title" ; }
}
```

**Which set of class definitions compiles?**

- A) `public interface Story extends SInt {}` / `public interface Art extends SInt {}`
- B) `sealed interface Story extends SInt {}` / `non-sealed class Art implements SInt {}`
- C) `non-sealed interface Story extends SInt {}` / `non-sealed interface Art extends SInt {}`- D) `interface Story extends SInt {}` / `interface Art extends SInt {}`
- E) `non-sealed interface Story extends SInt {}` / `class Art implements SInt {}`

---

### Pregunta 46 (Page 46 of 50)
**Given:**
```java
interface IFace {
    public void m1();
    public default void m2() {
        System.out.println("m2");
    }
    public static void m3() {
        System.out.println("m3");
    }
    private void m4() {
        System.out.println("m4");
    }
}

class MyC implements IFace {
    public void m1() {
        System.out.println("Hello");
    }
}
```

**Which two method invocations execute?**

- A) `IFace myClassObj = new MyC();` / `myClassObj.m4();`
- B) `IFace myClassObj = new MyC();` / `myClassObj.m3();`
- C) `IFace.m3();`
- D) `IFace.m4();`
- E) `IFace.m2();`
- F) `new MyC().m2();`

---

---

### Pregunta 49 (Page 49 of 50)
**Assume you have an automatic module from the module path `display-ascii-0.2.jar`.**

**Which name is given to the automatic module based on the given JAR file?**

- A) display-ascii
- B) display.ascii- C) display-ascii-0.2
- D) display-ascii-0

---

### Pregunta 50 (Page 50 of 50)
**Which statement is true about migration?**

- A) The required modules migrate before the modules that depend on them in a top-down migration.
- B) Every module is moved to the module path in a top-down migration.
- C) Every module is moved to the module path in a bottom-up migration.
- D) Unnamed modules are automatic modules in a top-down migration.
