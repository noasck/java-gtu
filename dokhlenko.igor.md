```
- в общем и целом:
+ 18 баллов. это мне уже надоело искать ошибки. Делайте лабы вовремя.
```

# Java Mid-Term Exam

**Student:** დოხლენკო იგორ

**Student ID:** 1791595

**Cheating detected:** Yes

## Task 4

### Subtask 1

Что такое инкапсуляция (обе части определения)?

```
Инкапсуляция - это объединение данных и методов для работы с этими данными. Сокрытие внутренних механизмов работы класса.
```

### Subtask 2

Что такое модификаторы доступа? Зачем они нужны? Перечислить модификаторы доступа и их назначение.

```
Модификаторы доступа - это ключевые слова определяющие область видимости членов класса. Нужны для реализации инкапсуляции и безопасности данных

public - виден всем
private - виден внутри класса
package-private - виден внутри пакета
protected - виден наследникам
```

```diff
-безопасность данных - бред.
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
	private String username;

	// TODO: указать модификатор доступа
	private String passwordHash;

	// TODO: указать модификатор доступа
	public User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	// TODO: указать модификатор доступа
	public boolean checkPassword(String hash) {
		return passwordHash.equals(hash);
	}

	// TODO: указать модификатор доступа
	public String getUsername() {
		return username;
	}
}

class AdminUser extends User {

	// TODO: указать модификатор доступа
	private int accessLevel;

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

		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
		System.out.println(admin.getUsername());
		System.out.println(admin.checkPassword());
		System.out.println(admin.hasAccess());
		System.out.println(admin.getAccessLevel());
	}
}

```

**Output:**

```
Compilation error:
C:\Users\GTU-Student\Desktop\.\Main.java:56: error: method checkPassword in class User cannot be applied to given types;
		System.out.println(admin.checkPassword());
		                        ^
  required: String
  found:    no arguments
  reason: actual and formal argument lists differ in length
C:\Users\GTU-Student\Desktop\.\Main.java:57: error: method hasAccess in class AdminUser cannot be applied to given types;
		System.out.println(admin.hasAccess());
		                        ^
  required: int
  found:    no arguments
  reason: actual and formal argument lists differ in length
2 errors

```

```diff
- тут private неправильно:
// TODO: указать модификатор доступа
	private String username;

	// TODO: указать модификатор доступа
	private String passwordHash;
@@@ и ваш код не компилится...
```


## Task 6

### Subtask 1

Дать определение понятию “конструктор класса” в java. Что такое конструктор по умолчанию?

```
Конструктор класса в Java - это специальный блок кода, который вызывается при создании объекта для его инициализации
Конструктор по умолчанию (default constructor) - Это конструктор без аргументов, который компилятор добавляет в класс автоматически, только если программист не написал ни одного своего конструктора.
```

### Subtask 2

Почему есть конструктор но нет деструктора? Почему метод finalize никогда не стоит использовать?

```
В Java работает Garbage Collector. Он освобождает память от ненужного. Соответственно деструктор при этом не нужен
```
```diff
- AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ДА ПРИЧЁМ ЗДЕСЬ КОЛЛЕКТОР???????????

@@@ ЛЮДИ, ВЫ ОТКУДА?


⣩⡝⠟⣩⣶⣶⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⡟⣉⢻⢡⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿
⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡿⠟⠃⣛⣀⣚⡃⠻⢿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠟⣡⣶⣿⣿⣿⣿⣿⣿⣿⣷⣮⡙⢿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⡿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣥⣾⣬⡴⠠⠿⢿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⡧
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣾⣿⣿⣿⣿⣿⣿⣿⠟⣻⣿⣿⣿⣿⡇⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⠿⠟⣩⣴⣿⣿⣿⣿⣷⣶⣃⡈⣹⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⡿⢁⣿⡿⢻⣿⣿⣿⡿⢛⡛⢿⣿⣿⠇⣿⣿⣿⣿⢸⣿⣿⡿⡋⢭⣭⣤⡒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⡥⣨⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣸⢸⠇⡏⡿⢠⢸⣿⣿⢏⣾⣿⣿⣦⡹⣿⢸⣿⣿⣿⣿⢸⣿⣿⢰⢓⣚⢻⣿⡿⠌⠿⠿⣿⡿⢿⣿⣿⣿⣿⣯⡶⢃⣛⢻⣿⣿⣷⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡇⡄⠜⠃⢡⣿⢸⣿⣿⠸⣿⣿⣿⣿⡇⢠⣼⣿⣿⣿⣿⠸⢟⣩⣦⠻⣿⣧⠉⣴⣿⣿⣿⣦⡙⣦⠙⣿⣿⣿⣿⣿⣟⣁⡚⣻⣿⣿⢸⣿⣿⣿⡿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢱⡧⣧⣄⣾⣿⣿⣿⣿⣧⣙⠻⠿⠟⣃⣚⡛⢿⣿⣿⡏⠴⠻⢿⣿⣶⣿⣿⡸⣿⣿⣏⣩⣿⡇⣽⣶⣿⣿⣿⣿⣿⣟⣁⠺⣿⣿⣿⢸⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣼⣷⡶⢒⣭⣶⣶⣿⣿⣶⣶⣤⣍⡛⠿⣿⣿⢆⣿⣿⣿⡘⠌⡂⣍⠻⣿⣿⣷⣘⠿⠿⠿⢟⣱⣿⣿⣿⣿⣿⡿⢟⣫⣵⣾⣿⣿⣿⢸⣿⣿⣿⣇
⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⣡⣿⡿⢃⣴⣿⠿⠟⠻⠿⣿⣿⣿⣿⣿⣿⣇⢲⣶⣾⣿⣿⣿⣿⣦⡑⢨⠱⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣋⣵⣾⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⡏
⣿⣿⣿⣿⣿⡿⢋⣴⣿⣌⢿⣿⢣⣾⠏⠄⣾⡿⣡⣾⡦⡙⢿⣿⣿⣿⣧⢸⡿⠿⡿⠻⢿⣿⣿⣿⣦⡁⢬⠡⡙⣿⣿⣿⣿⡿⠟⣋⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⡇
⣿⣿⣿⠟⣋⡄⢿⣿⣿⣿⣦⡙⠸⣿⡘⠼⠋⠴⠿⣫⡾⢟⣠⣍⡻⠿⠟⠸⠇⣧⣰⡇⣾⡇⣿⣿⠁⠀⠰⡀⠐⠈⣯⢳⢒⡀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⡇
⡿⢋⣵⣾⣿⣿⡌⢿⣿⣿⣿⣿⣦⡈⠻⠷⣶⠶⠖⠒⢂⣸⣿⣿⣿⣿⣧⣝⢻⣿⠿⣧⡭⠅⣿⣿⣿⣧⣀⡁⡀⠀⢸⢀⣭⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⡇
⣴⣿⣿⣿⣿⣿⣿⣌⠻⣿⣿⣿⣿⣿⣷⣌⠛⡼⠂⣴⣶⣶⣶⣶⣶⣷⣶⣶⣶⣶⣦⣬⣬⣍⡉⠉⠄⠀⣀⣀⣁⣠⡼⣸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⠿⣗⣈⣭⣭⣭⣭⡭⢉⡁⡴⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⠾⠿⠿⣉⣄⢉⡉⠿⠿⠿⠿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣷
⣿⣿⣿⣿⣿⡟⣡⣾⣿⣿⣿⣿⣿⢏⣴⣶⣤⣥⣭⣟⣛⣛⣛⣛⣛⣛⣛⣛⣿⣭⣭⣥⣴⣶⣦⣽⣿⣤⣾⡇⣾⣿⠟⠈⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢱⣿⣿⣿⣿⣿⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣴⣶⣾⠆⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣩⣭⣭⡄⠀⠀⠀⠀⣠⠀⢀⣘⠛⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⠹⣿⣿⣿⣿⣿⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⡿⠧⠛⣛⣛⣄⣀⣀⣠⣤⡿⢹⣿⣧⠌⢻⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣮⣙⠿⠿⢿⣧⡘⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣛⣋⣭⣴⣶⣿⣿⣿⣦⣘⠿⢿⣿⣿⣿⣿⣿⣿⠷⠿⠿⡷⢄⣶⣤⣭⣭⣭⣭⣍⣃⢩⣭⣴⣶
```


### Subtask 3

Наследуются ли конструкторы? Как вызвать конструктор родительского класса?

```
Конструктор не наследуется. Его можно только вызвать, используя super()
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

```

```diff
- даже не попробовали.
-4 балла.
```


## Task 10

### Subtask 1

Дать определение полиморфизма типов в Java.

```
способность системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта
```

### Subtask 2

Сравнить тип объекта и тип ссылки в Java (Pointer type vs Object type). Подсказка: это имеет отношение к переопределению методов.

```
Тип объекта определяет как метод выполнится в RunTime,в то время как тип ссылки определяет какие методы можно вызвать.
```

### Subtask 3

Как устроен специальный (параметрический) полиморфизм в джава? Как называется обеспечивающий его механизм

```
Позволяет писать классы и методы, работающие с разными типами данных, передавая тип как параметр. Он реализован в Джава через стирание типов - информация о дженериках удаляется при компиляции.
```
```diff
- бред из чата ГПТ
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
