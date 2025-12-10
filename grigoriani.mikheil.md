<code style="color : red">
в общем - 27/30
</code>


# Java Mid-Term Exam

**Student:** გრიგორიანი მიხეილ

**Student ID:** 1401884

**Cheating detected:** No

## Task 1

### Subtask 1

Дать определение JVM, JRE, JDK. Расшифровка каждой аббревиатуры, назначение и взаимосвязь.

```
JRE - Java runtime environment. Джава среда, необходимая для запуска джава файлов, имеет в себе стандартный набор джава библиотек (джава классы) и JVM
JDK - Java development kit. Набор инструментов и библиотек, необходимых для разработки и компиляции джава кода (например, javac). Имеет в себе JRE и JVM
JVM - Java virtual machine. Виртуальная машина, которая запускает байт код.
```

<code style="color : red">
2
</code>
### Subtask 2

Проблема платформозависимости: почему нужно компилировать код по-разному для каждой операционной системы и какие неудобства с этим связаны?

```
Код нужно компилировать по-разному для каждой операционной системы, потому что ОС отличаются архитектурой друг от друга. Неудобств, связанных с этим много, код для каждой системы нужно писать заново или переделывать старый, а так как операционок может быть неограниченное количество и не ясно, какой конкретно будет пользоваться юзер, это может вылиться в огромные проблемы для разработчика.
```

<code style="color : red">
1, нет про архитектуры разные, и необязательно код надо переделывать, там и без этого проблем хватает.
</code>
### Subtask 3

Мотивация создания JVM и диаграмма процесса компиляции и исполнения: машинный код, исходный код, байт-код.

```
Создание JVM было мотивировано проблемой платформозависимости, оно было обосновано принципом write once-run everywhere. JVM платформазависима, но компилирует байт код вне зависимости от системы.
Процесс компиляции и исполнения следующий: исходный код, написанный разработчиком, компилируется (JIT компиляцией) в байт-код, после чего компилируется в машинный код JVM в зависимости от системы.
```

<code style="color : red">
1.5/2. wora плюс, но где вы JIT там в байт-коде взяли? ай ай ай, ну хоть бы не писали совсем. Почитайте что такое JIT.
</code>
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
	public static int objectsPrinted;

	public Printer3D(String model, int filamentLevel, int powerLevel){
		this.model = model;
		if(filamentLevel > 0){
			this.filamentLevel = filamentLevel;
		}else{
			this.filamentLevel = 0;
		}
		if(powerLevel > 0){
			this.powerLevel = powerLevel;
		}else{
			this.powerLevel = 0;
		}
	}
	public void refillFilament(int amount){
		if(amount <= 0){
			System.out.println("Filament level must be positive.");
			return;
		}
		this.filamentLevel += amount;
	}
	public void recharge(int amount){
		if(amount <= 0){
			System.out.println("Power level must be positive");
			return;
		}
		this.powerLevel += amount;
	}
	public void printObject(int filamentNeeded, int powerNeeded){
		if(filamentNeeded > this.filamentLevel || powerNeeded > this.powerLevel){
			System.out.println("Not enough resources");
			return;
		}
		this.filamentLevel -= filamentNeeded;
		this.powerLevel -= powerNeeded;
		objectsPrinted++;
		System.out.println("Object successfully printed");
	}
	public void printStatus(){
		System.out.println("Filament level: " + this.filamentLevel);
		System.out.println("Power level: " + this.powerLevel);
		System.out.println("Number of printed objects:" + objectsPrinted);
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
Filament level: 500
Power level: 80
Number of printed objects:0
Object successfully printed
Object successfully printed

Filament level: 350
Power level: 50
Number of printed objects:2

```

<code style="color : red">
смогли. 4
</code>

## Task 7

### Subtask 1

Статические поля - определение и их свойства. Статические методы - определение и их свойства.

```
Статическое поле - это поле, общее для всех экземпляров класса. Обращаться к нему следует напрямую через название класса.
Статический метод - это метод, который не требует экземпляра класса для вызова. Пример статического метода: Math.pow(), Math.sqrt()
```

<code style="color : red">
как-то очень кратко и общО. 1.5/2
</code>
### Subtask 2

Зачем нужны статические члены класса? Приведите пример, где это может понадобиться.

```
Статические члены класса нужны, когда не нужно создание экземпляра класса для вызова. Например, классу Math не нужно создание экземпляра Math для вызова его методов, поэтому почти все они статичны, так же как и поля констант, к примеру Math.PI.
```
<code style="color : red">
Где-то рядом, но это далеко не единственное.
1/2
</code>

### Subtask 3

Статические импорты - что это и зачем нужно

```
Статические импорты это импорты, облегчающие написание кода. Нужно чтобы не вызывать методы импортированного класса через название класса, а напрямую:
import static Math.*;
Вместо Math.sqrt(num) теперь sqrt(num).
```

<code style="color : red">
Где-то рядом, но это далеко не единственное.
1/2
</code>
### Subtask 4

Дано описание вспомогательного класса из реального мира — помощник логов.<br>
Необходимо реализовать класс <code>LogHelper</code>.<br><br>

<b>Описание класса LogHelper</b><br><br>

Класс должен работать <b>только через статические поля и методы</b>.<br><br>

<b>Статические поля:</b><br>
<ul>
	<li><code>logLevel</code> — текущий уровень логирования (int)<br>
	Например: 1 — только ошибки, 2 — ошибки и предупреждения, 3 — все сообщения</li>
	<li><code>prefix</code> — префикс для всех лог-сообщений (строка)</li>
	<li><code>logsCount</code> — количество выведенных лог-сообщений (int)</li>
</ul>

<b>Статические методы:</b><br><br>

<code>configure(int level, String pref)</code><br>
Настраивает уровень логирования и префикс.<br>
Сохраняет значения в соответствующие статические поля.<br><br>

<code>log(int level, String message)</code><br>
Выводит сообщение в консоль, если <code>level &lt;= logLevel</code>.<br>
Формат вывода (пример):<br>
<code>[LEVEL 2][APP] Запуск модуля</code><br><br>
Если сообщение выведено — увеличивает <code>logsCount</code>.<br>
Если сообщение не выведено — ничего не меняет.<br><br>

<code>setPrefix(String pref)</code><br>
Меняет текущий префикс.<br><br>

<code>setLevel(int level)</code><br>
Меняет текущий уровень логирования.<br><br>

<code>printStatus()</code><br>
Выводит текущие значения уровня логирования, префикса и количества выведенных сообщений.


```java
class LogHelper {
	private static int logLevel;
	private static String prefix;
	private static int logsCount;

	public static void configure(int level, String pref){
		logLevel = level;
		prefix = pref;
	}
	public static void log(int level, String message){
		if(level <= logLevel){
			System.out.println("[LEVEL " + level + "] [" + prefix + "] " + message);
			logsCount++;
		}
	}
	public static void setPrefix(String pref){
		prefix = pref;
	}
	public static void setLevel(int level){
		logLevel = level;
	}
	public static void printStatus(){
		System.out.println("Log level: " + logLevel);
		if(prefix == null){
			System.out.println("Prefix not set");
		}else{
			System.out.println("Prefix: " + prefix);
		}
		System.out.println("Logs count: " + logsCount);
	}
}

public class Main {
	public static void main(String[] args) {
		LogHelper.configure(2, "APP");

		LogHelper.printStatus();
		LogHelper.log(1, "Критическая ошибка");
		LogHelper.log(3, "Отладочная информация");

		System.out.println();

		LogHelper.setLevel(3);
		LogHelper.setPrefix("CORE");

		LogHelper.printStatus();
		LogHelper.log(2, "warning");
	}
}

```

**Output:**

```
Log level: 2
Prefix: APP
Logs count: 0
[LEVEL 1] [APP] ����������� ������

Log level: 3
Prefix: CORE
Logs count: 1
[LEVEL 2] [CORE] warning

```

<code style="color : red">
Хороший код. запускается, супер. 4.
</code>

## Task 11

### Subtask 1

Что такое абстрактные классы? Что такое абстрактные методы?

```
Абстрактный класс - это
Абстрактный метод - это
```

### Subtask 2

Зачем нужны абстрактные классы?

```

```

### Subtask 3

Как наследуются абстрактные методы? Разрешено ли множественное наследование абстрактных классов?

```

```

### Subtask 4

Вам дан рабочий класс <code>Main</code> и два класса предметов: <code>Sword</code> и <code>Staff</code>, а также пустой базовый класс <code>Item</code>.<br>
Код частично работает, но содержит ошибки проектирования и компиляции.<br>
Ваша задача — починить программу, вынеся общее поведение в базовый класс <code>Item</code>.<br><br>

<b>Требуется:</b><br><br>

<b>1. Перенести общее в родительский класс</b><br>
В классах <code>Sword</code> и <code>Staff</code> есть повторяющиеся поля и методы:<br>
<ul>
	<li><code>name</code></li>
	<li><code>weight</code></li>
	<li><code>durability</code></li>
	<li>метод <code>repair(int amount)</code></li>
	<li>часть логики метода <code>use()</code> (например, уменьшение <code>durability</code>)</li>
</ul>
Вынесите всё общее в базовый класс <code>Item</code>.<br><br>

<b>2. Настроить корректное наследование</b><br>
<ul>
	<li>Класс <code>Item</code> должен иметь конструктор</li>
	<li>В дочерних классах (<code>Sword</code>, <code>Staff</code>) конструктор должен вызывать родительский через <code>super(...)</code></li>
</ul>


```java
public class Main {
	public static void main(String[] args) {
		Sword sword = new Sword("Excalibur", 5.0, 100, 25);
		Staff staff = new Staff("Elder Staff", 3.0, 120, 40);

		sword.use();
		staff.use();

		System.out.println();

		Item[] items = { sword, staff };

		for (Item it : items) {
			it.repair(5);
			it.use();
			System.out.println();
		}

		System.out.println(sword.durability);
	}
}

class Item {
}

class Sword extends Item {
	public String name;
	public double weight;
	public int durability;
	public int damage;

	public Sword(String name, double weight, int durability, int damage) {
		super();
		this.name = name;
		this.weight = weight;
		this.durability = durability;
		this.damage = damage;
	}

	public void repair(int amount) {
		durability += amount;
		System.out.println(name + " repaired by " + amount + ". Durability=" + durability);
	}

	public void use() {
		System.out.println(name + " slashes for " + damage + " damage!");
		durability -= 1;
	}
}

class Staff extends Item {
	public String name;
	public double weight;
	public int durability;
	public int manaBonus;

	public Staff(String name, double weight, int durability, int manaBonus) {
		super();
		this.name = name;
		this.weight = weight;
		this.durability = durability;
		this.manaBonus = manaBonus;
	}

	public void repair(int amount) {
		durability += amount;
		System.out.println(name + " repaired by " + amount + ". Durability=" + durability);
	}

	public void use() {
		System.out.println(name + " channels magic with +" + manaBonus + " mana!");
		durability -= 1;
	}
}


```

**Output:**

```

```
