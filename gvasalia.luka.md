```diff
- в общем и целом - 25/30
```


# Java Mid-Term Exam

**Student:** გვასალია ლუკა

**Student ID:** 1705583

**Cheating detected:** Yes

## Task 4

### Subtask 1

Что такое инкапсуляция (обе части определения)?

```
Инкапсуляция - это ...praces sozdanie obiekta v pamiti pri pomashi operatera  new bizov konstruktara klasa.
```

```diff
-инициализация, не инкапсуляция.
```

### Subtask 2

Что такое модификаторы доступа? Зачем они нужны? Перечислить модификаторы доступа и их назначение.

```
Модификаторы доступа - это
eto kluchivie slova b java kotorie ustanavlivaiut urovin vidimosti dlia chlenov klasa v samix klasax
public - dostup otavsudu
private - dostup predelax sbibo klasa
package-private -dostup tolko b predelax svovo paketa
protected -dostup  v predelax  cvovo paketa  iz bsex podklasov
```

### Subtask 3

Вам даны два класса: <code>User</code> и <code>AdminUser</code>, а также тестирующий класс <code>Main</code>.<br><br>

В коде присутствуют комментарии <code>// TODO: поставить уровень доступа</code>.<br>
Необходимо заменить их на корректные модификаторы доступа (<code>public</code>, <code>protected</code>, <code>private</code>) так, чтобы соблюсти принцип <b>минимального раскрытия</b> (<i>least privilege</i>).<br><br>

<b>Требуется:</b><br>
<ul>
	<li>Скрыть все поля, которые не должны быть доступны напрямую</li>
	<li>Оставить доступ только там, где он действительно необходим</li>
	<li>Учитывать наследование класса <code>AdminUser</code> от <code>User</code></li>
	<li>Обеспечить корректную работу кода в классе <code>Main</code></li>
</ul>

<b>Примечание:</b><br>
В классе <code>Main</code> необходимо вызывать только те поля и методы, которые вы сочли публичными.


```java
class User {

	// TODO: указать модификатор доступа
	protected String username;

	// TODO: указать модификатор доступа
	private String passwordHash;

	// TODO: указать модификатор доступа
	public User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	// TODO: указать модификатор доступа
	public boolean checkPassword(String hash) {
		return this. passwordHash.equals(hash);
	}

	// TODO: указать модификатор доступа
	public String getUsername() {
		return username;
	}
}

class AdminUser extends User {

	// TODO: указать модификатор доступа
	protected int accessLevel;

	// TODO: указать модификатор доступа
	public AdminUser(String username, String passwordHash, int accessLevel) {
		super(username, passwordHash);
		this.accessLevel = accessLevel;
	}

	// TODO: указать модификатор доступа
	public boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	// TODO: указать модификатор доступа
	public int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);
		Sistem.out.println("Username:" + admin. getusername());
		Sistem.out.println("Check password" ('12312321'):+admin.checkpassword
		Sistem.out.println("Check password"('wrong'):+admin.checkpassword('wrong'));
		Sistem.out.println("Access Level:"+ admin.getAccessLevel());




		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
	}
}

```

**Output:**

```

```

```
-немного бред, но рациональное зерно где-то есть. 2/4
```


## Task 6

### Subtask 1

Дать определение понятию “конструктор класса” в java. Что такое конструктор по умолчанию?

```
Конструктор класса в Java - это ... cpecialni blok koda paxoji na metod kotori ispozuitsia dlia cozdanie obiekta klasaa inicializacii
Конструктор по умолчанию (default constructor) - eto  konstruktor bez parametrov kotirie avtomatitiski generiruiut kompiliari java dlia klasa ecli vi ne opridelili b nem  ne odnovo cobstbibova konstriktora
```

### Subtask 2

Почему есть конструктор но нет деструктора? Почему метод finalize никогда не стоит использовать?

```
1)avtomatiteski sbros munsora
2)evo bizob ne garantiruer i neprdskazuem sgto negatrivno vliat na programi
```
```diff
-да кто вам про этот сбор мусора "посоветовал" написать? 10 из 10 работ - неправильный ответ. 1/2
```
### Subtask 3

Наследуются ли конструкторы? Как вызвать конструктор родительского класса?

```
net ni nasleduit
spomashiu kluchivova slova super(..)
```

### Subtask 4

Дано описание предмета из реального мира.<br>
Необходимо реализовать класс <b>Printer3D</b>.<br><br>

<b>Описание класса Printer3D</b><br><br>

<b>Поля</b><br>
<ul>
	<li><code>model</code> — модель принтера (строка)</li>
	<li><code>filamentLevel</code> — текущий уровень филамента в граммах (int)</li>
	<li><code>powerLevel</code> — уровень заряда принтера в процентах (int)</li>
	<li><code>objectsPrinted</code> — количество напечатанных объектов (int)</li>
</ul>

<b>Конструктор</b><br>
Принимает:<br>
<ul>
	<li>модель принтера</li>
	<li>стартовый уровень филамента</li>
	<li>стартовый уровень заряда</li>
</ul>

<b>Методы</b><br><br>

<code>printObject(int filamentNeeded, int powerNeeded)</code><br>
Печатает объект, если хватает ресурсов.<br>
Уменьшает уровень филамента и заряда.<br>
Увеличивает счётчик <code>objectsPrinted</code>.<br>
Выводит сообщение об успешной печати или об ошибке.<br><br>

<code>refillFilament(int amount)</code><br>
Добавляет филамент.<br><br>

<code>recharge(int amount)</code><br>
Добавляет заряд.<br><br>

<code>printStatus()</code><br>
Выводит текущие уровни филамента, заряд и количество напечатанных объектов.


```java
class Printer3D {
	private string model;
	private int filamentLevel;
	private int powerLevel;
	private int objectsprinted;

	public Printer3D(String m, int f, int p){
		this.m = m; this.f = f; this.p = p; this.o =0;
		Sistem.out.println
	}

}

public class Main {
	public static void main(String[] args) {
		Printer3D printer = new Printer3D("Creality Ender 3", 500, 80);

		printer.printStatus();
		printer.printObject(50, 10);
		printer.printObject(200, 40);

		System.out.println();

		printer.refillFilament(100);
		printer.recharge(20);

		printer.printStatus();
	}
}

```

**Output:**

```
Compilation error:
C:\Users\GTU-512B-724A\Desktop\.\Main.java:2: error: cannot find symbol
	private string model;
	        ^
  symbol:   class string
  location: class Printer3D
C:\Users\GTU-512B-724A\Desktop\.\Main.java:13: error: constructor Printer3D in class Printer3D cannot be applied to given types;
		Printer3D printer = new Printer3D("Creality Ender 3", 500, 80);
		                    ^
  required: no arguments
  found:    String,int,int
  reason: actual and formal argument lists differ in length
C:\Users\GTU-512B-724A\Desktop\.\Main.java:15: error: cannot find symbol
		printer.printStatus();
		       ^
  symbol:   method printStatus()
  location: variable printer of type Printer3D
C:\Users\GTU-512B-724A\Desktop\.\Main.java:16: error: cannot find symbol
		printer.printObject(50, 10);
		       ^
  symbol:   method printObject(int,int)
  location: variable printer of type Printer3D
C:\Users\GTU-512B-724A\Desktop\.\Main.java:17: error: cannot find symbol
		printer.printObject(200, 40);
		       ^
  symbol:   method printObject(int,int)
  location: variable printer of type Printer3D
C:\Users\GTU-512B-724A\Desktop\.\Main.java:21: error: cannot find symbol
		printer.refillFilament(100);
		       ^
  symbol:   method refillFilament(int)
  location: variable printer of type Printer3D
C:\Users\GTU-512B-724A\Desktop\.\Main.java:22: error: cannot find symbol
		printer.recharge(20);
		       ^
  symbol:   method recharge(int)
  location: variable printer of type Printer3D
C:\Users\GTU-512B-724A\Desktop\.\Main.java:24: error: cannot find symbol
		printer.printStatus();
		       ^
  symbol:   method printStatus()
  location: variable printer of type Printer3D
8 errors

```

```diff
-много ошибок. 2/4
-вам не нужно было делать задание ниже, у вас сданы все лабораторные работы.
```


## Task 10

### Subtask 1

Дать определение полиморфизма типов в Java.

```
eto cposobnost obiekta prinimat neskalko  porm lil cpocobnost metoda deistvovat po raznamu v zavisimosti ot tipa obiekta, k katoromu on prinimaitia
```

### Subtask 2

Сравнить тип объекта и тип ссылки в Java (Pointer type vs Object type). Подсказка: это имеет отношение к переопределению методов.

```
1)tip cilki opridilat kakie metodi dostupni dlia vizova 2)tip obiekta opridelaet kakaia realizacia metada budet vipolnina
```

### Subtask 3

Как устроен специальный (параметрический) полиморфизм в джава? Как называется обеспечивающий его механизм

```
1)eto fundamentalni koncepcia v teori tipov , kotoraia pozvalaet funkcii ili tipa dannix  bit napisanami ababshona .tak shtobi on mog abrabatavatznachenia bez zavisimosti
```

### Subtask 4

<b>Задача</b><br><br>

Вам дан рабочий класс <code>Main</code> и два класса компонентов:
<code>RenderComponent</code> и <code>PhysicsComponent</code>,
а также пустой базовый класс <code>Component</code>.<br><br>

Код частично работает, но содержит ошибки проектирования и дублирование.<br>
Ваша задача — исправить программу, вынеся общее поведение в базовый класс
<code>Component</code>.<br><br>

<b>Требуется:</b><br><br>

<b>1. Перенести общее в родительский класс</b><br>
В классах <code>RenderComponent</code> и <code>PhysicsComponent</code>
повторяются поля и методы:<br>
<ul>
	<li><code>id</code></li>
	<li><code>enabled</code></li>
	<li><code>priority</code></li>
	<li>методы <code>enable()</code> и <code>disable()</code></li>
	<li>часть логики метода <code>update()</code>
	(например, проверка <code>enabled</code> и уменьшение <code>priority</code>)</li>
</ul>
Вынесите всё общее в базовый класс <code>Component</code>.<br><br>

<b>2. Настроить корректное наследование</b><br>
<ul>
	<li>Класс <code>Component</code> должен иметь конструктор</li>
	<li>В дочерних классах
	(<code>RenderComponent</code>, <code>PhysicsComponent</code>)
	конструктор должен вызывать родительский через <code>super(...)</code></li>
</ul>


```java
public class Main {
    public static void main(String[] args) {
        RenderComponent rc = new RenderComponent("Renderer", true, 5, "Mesh_A");
        PhysicsComponent pc = new PhysicsComponent("Physics", true, 3, 0.98);

        rc.update();
        pc.update();

        System.out.println();

        Component[] components = { rc, pc };

        for (Component c : components) {
            c.disable();
            c.update();
            System.out.println();
        }

        System.out.println(rc.priority);
    }
}

class Component {
	public String id;
    public boolean enabled;
    public int priority;
    Component(String id, boolean enabled, int priority){
		this.id = id;
		this.id = enabled;
		this.id = priority;
    }
    public void enable() {
        enabled = true;
        System.out.println(id + " enabled");
    }

    public void disable() {
        enabled = false;
        System.out.println(id + " disabled");
    }

    public void update() {
        if (!enabled) {
            System.out.println(id + " is disabled, skipping update");
            return;
        }
        System.out.println(id + " renders mesh " + meshName);
        priority -= 1;
    }
}


class RenderComponent extends Component {
    public String id;
    public boolean enabled;
    public int priority;
    public String meshName;
     public void enable() {
        enabled = true;
        System.out.println(id + " enabled");
    }

    public void disable() {
        enabled = false;
        System.out.println(id + " disabled");
    }

    public void update() {
        if (!enabled) {
            System.out.println(id + " is disabled, skipping update");
            return;
        }
        System.out.println(id + " applies physics with damping=" + damping);
        priority -= 1;
    }

    public RenderComponent(String id, boolean enabled, int priority, String meshName) {
        super( id, enabled,  priority  );
        this.meshName = meshName;

    }

}

class PhysicsComponent extends Component {
    public String id;
    public boolean enabled;
    public int priority;
    public double damping;


    public PhysicsComponent(String id, boolean enabled, int priority, double damping) {
        super(id,enabled,priority);
        this.damping = damping;
    }


}

```

**Output:**

```
Compilation error:
C:\Users\GTU-512B-724A\Desktop\.\Main.java:29: error: incompatible types: boolean cannot be converted to String
		this.id = enabled;
		          ^
C:\Users\GTU-512B-724A\Desktop\.\Main.java:30: error: incompatible types: int cannot be converted to String
		this.id = priority;
		          ^
C:\Users\GTU-512B-724A\Desktop\.\Main.java:47: error: cannot find symbol
        System.out.println(id + " renders mesh " + meshName);
                                                   ^
  symbol:   variable meshName
  location: class Component
C:\Users\GTU-512B-724A\Desktop\.\Main.java:73: error: cannot find symbol
        System.out.println(id + " applies physics with damping=" + damping);
                                                                   ^
  symbol:   variable damping
  location: class RenderComponent
4 errors

```
