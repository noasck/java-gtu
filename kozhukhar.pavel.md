``` diff
- 14/30
+ Постарайтесь подтянуть знания. Дальше сложнее темы. Смотрите видео, делайте задачи. Главное, занимайтесь каждый день по чуть-чуть.
         ,--"""",--.__,---[],-------._
       ,"   __,'            \         \--""""""==;-
     ," _,-"  "/---.___     \       ___\   ,-'',"
    /,-'      / ;. ,.--'-.__\  _,-"" ,| `,'   /
   /``""""-._/,-|:\       []\,' ```-/:;-. `. /
             `  ;:::      ||       /:,;  `-.\
                =.,'__,---||-.____',.=
                =(:\_     ||__    ):)=
               ,"::::`----||::`--':::"._
             ,':::::::::::||::::::::::::'.
    .__     ;:::.-.:::::__||___:::::.-.:::\     __,
       """-;:::( O )::::>_|| _<::::( O )::::-"""
   =======;:::::`-`:::::::||':::::::`-`:::::\=======
    ,--"";:::_____________||______________::::""----.          , ,
         ; ::`._(    |    |||     |   )_,'::::\_,,,,,,,,,,____/,'_,
       ,;    :::`--._|____[]|_____|_.-'::::::::::::::::::::::::);_
      ;/ /      :::::::::,||,:::::::::::::::::::::::::::::::::::/
     /; ``''''----------/,'/,__,,,,,____:::::::::::::::::::::,"
     ;/                :);/|_;| ,--.. . ```-.:::::::::::::_,"
    /;                :::):__,'//""\\. ,--.. \:::,:::::_,"
   ;/              :::::/ . . . . . . //""\\. \::":__,"
   ;/          :::::::,' . . . . . . . . . . .:`::\
   ';      :::::::__,'. ,--.. . .,--. . . . . .:`::`
   ';   __,..--'''-. . //""\\. .//""\\ . ,--.. :`:::`
   ;    /  \\ .//""\\ . . . . . . . . . //""\\. :`::`
   ;   /       . . . . . . . . . . . . . . . . .:`::`
   ;   (          . . . . . . . . . . . . . . . ;:::`
   ,:  ;,            . . . . . . . . . . . . . ;':::`
   ,:  ;,             . . . . . . . . . . . . .;`:::
   ,:   ;,             . . . . . . . . . . . . ;`::;`
    ,:  ;             . . . . . . . . . . . . ;':::;`
     :   ;             . . . . . . . . . . . ,':::;
      :   '.          . . . . . . . .. . . .,':::;`
       :    `.       . . . . . . . . . . . ;::::;`
        '.    `-.   . . . . . . . . . . ,-'::::;
          `:_    ``--..___________..--'':::::;'`
             `._::,.:,.:,:_ctr_:,:,.::,.:_;'`
________________`"\/"\/\/'""""`\/"\/""\/"____________________________


```


# Java Mid-Term Exam

**Student:** კოჟუხარ პაველ

**Student ID:** 1848960

**Cheating detected:** Yes

## Task 1

### Subtask 1

Дать определение JVM, JRE, JDK. Расшифровка каждой аббревиатуры, назначение и взаимосвязь.

```
JRE - среда выполнения.  Нужна чтобы запустить программу
JDK - Java Development Kit. Нужен чтобы написать программу
JVM - Java virtual machine. Программа, которая читает байт коды
```

```diff
- ну а расшифровка JRE?
```

### Subtask 2

Проблема платформозависимости: почему нужно компилировать код по-разному для каждой операционной системы и какие неудобства с этим связаны?

```
потому что каждая система по своему общается
```

```diff
- общается с космосом?
```

### Subtask 3

Мотивация создания JVM и диаграмма процесса компиляции и исполнения: машинный код, исходный код, байт-код.

```
основная мотивация написал один раз - запускай везде
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
	string model;
	int filamentLevel;
	int powerLevel;
	int objectsPrinted;

	public Printed3d(String model, int filamentLevel, int powerLevel){
			this.model = model;
			this.filamentLevel = filamentLevel;
			this.powerLevel = powerLevel;
			this.objectsPrinted = 0;
		}
	public void printObject(int filamentLevel, int powerNeeded){
			if (filamentLevel>= filamentNeeded && powerLevel >= powerNeeded) {
				filamentLevel-= filamentNeeded;
				powerLevel -= powerNeeded;
				objectPrinted++;
				System.out.printIn("напечатан");
				} else {
					System.out.printIn("ошибка не достаточно ресурсов");
					}
		}
		public void refillfilament(int amount) {
			filamentLevel += amount;
			}
		public void printStatus() {
		System.out.printIn("модель" + model);
		System.out.printIn("филамент" + filamentLevel + " r");
		System.out.printIn("заряд" + powerLevel  + " %");
		System.out.printIn("наапечатано объектов"  + objectPrinted);
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
C:\Users\GTU-Student\Desktop\java\.\Main.java:7: error: invalid method declaration; return type required
	public Printed3d(String model, int filamentLevel, int powerLevel){
	       ^
1 error

```diff
- не компилится. 3/4
```



## Task 7

### Subtask 1

Статические поля - определение и их свойства. Статические методы - определение и их свойства.

```
Статическое поле - это переменная, которая принадлежит своему классу на конкретном объекте
Статический метод - это метод, который можно вызвать без создания объекта
свойство: существует в единственном в экземпляре памяти
```

### Subtask 2

Зачем нужны статические члены класса? Приведите пример, где это может понадобиться.

```
нельзя использовать this и обращаться к нестатическим методам
```

### Subtask 3

Статические импорты - что это и зачем нужно

```
позволяет использовать статистические поля и методы другого класса без указания класса
```

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

```


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
