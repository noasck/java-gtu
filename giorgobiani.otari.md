<code style="color : red"> Ну в общем, 29/30 </code>
$${\color{red}
Ну в общем, 29/30
}$$
# Java Mid-Term Exam

**Student:** გიორგობიანი ოთარი

**Student ID:** 1877350

**Cheating detected:** No

## Task 4

### Subtask 1

Что такое инкапсуляция (обе части определения)?

```
Инкапсуляция - объединение полей и методов для работы с этими данными
Также это ограничение доступа внутренних механизмов работы для обеспечения простоты использования
```

**COMMENT FROM LECTOR: Мда. 3. "
### Subtask 2

Что такое модификаторы доступа? Зачем они нужны? Перечислить модификаторы доступа и их назначение.

```
Модификаторы доступа - это специальные слова, для ограничения видимости классов их полей и методов.

public - модификатор, который делает, чтобы элемент был виден везде (доспуп из любой части программы)
private - модификатор, который делает, чтобы элемент был виден только в этом же классе (используется для ограничения доступа к классам, методам или полям для кода за пределами этого класса)
package-private - модификатор, который делает, чтобы элемент был виден в этом же пакете (испульзуется если в классе не указан никакой модификатор)
protected - модификатор, который делает, чтобы элемент был виден в том же пакете и его наследникам (обеспечивает доступ наследникам, но в то же время, сохраняет защиту от внешного доступа)
```

**COMMENT FROM LECTOR: Вот зачем они нужны не понял если честно из ответа. Там нет правильного ответа, просто хотелось услышать ваше мнение: зачем людям вот все эти private public, etc. . 2.5/3"
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
	protected User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	// TODO: указать модификатор доступа
	protected boolean checkPassword(String hash) { // КОММЕНТ: уже второй человек с этим протектед здесь. ГПТ????
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

		AdminUser admin = new AdminUser("Otari", "Otari-G01", 5);

		System.out.println(admin.getUsername());
		System.out.println(admin.getAccessLevel());
		System.out.println(admin.hasAccess(10));


	}
}

```

**COMMENT FROM LECTOR: принято. 4.**


**Output:**

```
Otari
5
false

```


## Task 6

### Subtask 1

Дать определение понятию “конструктор класса” в java. Что такое конструктор по умолчанию?

```
Конструктор класса в Java - это специальный метод, который вызывается при создании объекта и отвечает за его начальную инициалицацию
Конструктор по умолчанию (default constructor) - это конструктор без параметров, который создается автоматически если в классе не определен не один другой конструктор.
```
<code style="color : red"> КОММЕНТ: 1/2. слишком общО и коротко. про new, про null и 0. </code>
### Subtask 2

Почему есть конструктор но нет деструктора? Почему метод finalize никогда не стоит использовать?

```
В Java нет деструктора, потому что память освобождает автоматический сборщик мусора Garbage Collector
Метод finalize устарел и работает ненадежно он может быть выполнен слишком поздно или не выполнен вообще. Также он сильно замедляет работу программы.
```

<code style="color : red"> КОММЕНТ: 1.5/2 вы сами себе противоречите. Деструктор никак не относится к освобождению памяти, откуда вы это взяли: </code>
### Subtask 3

Наследуются ли конструкторы? Как вызвать конструктор родительского класса?

```
Нет, конструкторы никогда не наследуются. Каждый класс должен объявить свой собственный конструктор.
Конструктор родительского класса можно вызватьвать при помощи ключевого слова super(), но он должен стоять на первой строчке в конструкторе дочернего класса.
```

<code style="color : red"> КОММЕНТ: о, это хорошо уже. 2/2</code>
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
	private String model;
	private int filamentLevel;
	private int powerLevel;
	private int objectsPrinted;

	public Printer3D(String model,int filamentLevel,int powerLevel){
		this.model = model;
		this.filamentLevel = filamentLevel;
		this.powerLevel = powerLevel;
		this.objectsPrinted = 0;
	}
	public void printObject(int filamentNeeded, int powerNeeded){
		if (filamentLevel >= filamentNeeded && powerLevel >= powerNeeded){
			filamentLevel-= filamentNeeded;
			powerLevel-= powerNeeded;
			objectsPrinted++;
			System.out.println("Obiect uspeshno napechatan");
		}
		else {
			System.out.println("Oshibka pechati: nedostatochno resursov");
		}
	}
	public void refillFilament(int amount){
		filamentLevel += amount;
			System.out.println("Filament dobavlen");
	}
	public void recharge (int amount){
		powerLevel += amount;
		System.out.println("Zariad dobavlen");
	}
	public void printStatus(){
		System.out.println("Model: " + model);
		System.out.println("Filament: " + filamentLevel + "gr.");
		System.out.println("Zariad: " + powerLevel + "%");
		System.out.println("Napechatito obiektov: " + objectsPrinted);
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
Model: Creality Ender 3
Filament: 500gr.
Zariad: 80%
Napechatito obiektov: 0
Obiect uspeshno napechatan
Obiect uspeshno napechatan

Filament dobavlen
Zariad dobavlen
Model: Creality Ender 3
Filament: 350gr.
Zariad: 50%
Napechatito obiektov: 2

⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉

```

<code style="color : red"> КОММЕНТ: да да. 4/4 </code>



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
