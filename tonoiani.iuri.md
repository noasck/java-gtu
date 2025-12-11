```diff
- В общем и целом:
+ 21/30.
```
# Java Mid-Term Exam

**Student:** ტონოიანი იური

**Student ID:** 1061946

**Cheating detected:** Yes

## Task 4

### Subtask 1

Что такое инкапсуляция (обе части определения)?

```
Инкапсуляция - позволяет скрывать данные от неправильного использования и
```
```diff
-и? и что?
```

### Subtask 2

Что такое модификаторы доступа? Зачем они нужны? Перечислить модификаторы доступа и их назначение.

```
Модификаторы доступа - это

public - доступен из всех классов и пакетов
private - только внутри класса
package-private - доступ только внутри пакета
protected - только внутри пакета и дочерних классах
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
	String username;

	// TODO: указать модификатор доступа
	String passwordHash;

	// TODO: указать модификатор доступа
	User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	// TODO: указать модификатор доступа
	boolean checkPassword(String hash) {
		return passwordHash.equals(hash);
	}

	// TODO: указать модификатор доступа
	String getUsername() {
		return username;
	}
}

class AdminUser extends User {

	// TODO: указать модификатор доступа
	int accessLevel;

	// TODO: указать модификатор доступа
	AdminUser(String username, String passwordHash, int accessLevel) {
		super(username, passwordHash);
		this.accessLevel = accessLevel;
	}

	// TODO: указать модификатор доступа
	boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	// TODO: указать модификатор доступа
	int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);

		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
	}
}

```

**Output:**

```

```

```diff
- 0/3
```


## Task 6

### Subtask 1

Дать определение понятию “конструктор класса” в java. Что такое конструктор по умолчанию?

```
Конструктор класса в Java - специальный метод который вызывается при создании обьекта
Конструктор по умолчанию (default constructor) - пустой
```
```diff
- пустой как этот ответ
```

### Subtask 2

Почему есть конструктор но нет деструктора? Почему метод finalize никогда не стоит использовать?

```
Деструктора нет, так как есть Garbage Collector, который автоматический удаляет неиспользованныне части кода.
```

```diff
- AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. Если я прочитаю ещё где-то про деструктор и GC - выстрелю. НУ КТО ВАМ ТАКОЕ ПИШЕТ.
- А Си? без GC и деструкторов нет.
- А python? Есть и GC и деструкторы.
+ 10 из 10 бред
```

### Subtask 3

Наследуются ли конструкторы? Как вызвать конструктор родительского класса?

```
Конструкторы не наследуются,вызвать конструкторв родительского класса можно через super().
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
	String model;
	Int filamentlevel;
	int powerLevel;
	public static int objectsPrinted;

	public Printer3D (String model, int fillamenLevel, int powerLevel) {
		this.model = model;
		this.filamentLevel = filamentLevel;
		this.powerLevel = powerLevel;
	}
		public void printObject(int filamentNedeed, int powerNeeded) {
			if (filamentLevel >= filaentNeeded && powerLevel >= powerNeeded) {
				filamentLevel -= filamentNeeded;
				powerLevel -= powerNeeded;
				objectsPrinted++;
				System.out.println("Success"); }
				else {
					System.println("Error");
				}
			}
		}
		public void refillFilament(int amount){
			filamentLevel += amount;
			System.out.println("Заряжен")
		}

		public void printStatus(){
			System.out.println(model);
			System.out.println(filamentLevel);
			System.out.println(powerLevel);
			System.out.println(objectsPrinted);
		}


	public Printer3D(String model


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

```diff
- ну тут хоть попытались
3/4
```

```

**Output:**

```
Compilation error:
C:\Users\GTU-Student\Desktop\New folder (3)\.\Main.java:23: error: unnamed classes are a preview feature and are disabled by default.
		public void refillFilament(int amount){
		       ^
  (use --enable-preview to enable unnamed classes)
C:\Users\GTU-Student\Desktop\New folder (3)\.\Main.java:25: error: ';' expected
			System.out.println("�������")
			                             ^
C:\Users\GTU-Student\Desktop\New folder (3)\.\Main.java:36: error: class, interface, enum, or record expected
	public Printer3D(String model
	       ^
3 errors

```


## Task 10

### Subtask 1

Дать определение полиморфизма типов в Java.

```

```

### Subtask 2

Сравнить тип объекта и тип ссылки в Java (Pointer type vs Object type). Подсказка: это имеет отношение к переопределению методов.

```

```

### Subtask 3

Как устроен специальный (параметрический) полиморфизм в джава? Как называется обеспечивающий его механизм

```

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
}

class RenderComponent extends Component {
    public String id;
    public boolean enabled;
    public int priority;
    public String meshName;

    public RenderComponent(String id, boolean enabled, int priority, String meshName) {
        super();
        this.id = id;
        this.enabled = enabled;
        this.priority = priority;
        this.meshName = meshName;
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

class PhysicsComponent extends Component {
    public String id;
    public boolean enabled;
    public int priority;
    public double damping;

    public PhysicsComponent(String id, boolean enabled, int priority, double damping) {
        super();
        this.id = id;
        this.enabled = enabled;
        this.priority = priority;
        this.damping = damping;
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
        System.out.println(id + " applies physics with damping=" + damping);
        priority -= 1;
    }
}

```

**Output:**

```

```
