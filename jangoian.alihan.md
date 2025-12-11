```diff
- в общем и целом: 24/30
+ подтяните решение практических заданий. Вы же программист будущий
```

# Java Mid-Term Exam

**Student:** ჯანგოიან ალხან

**Student ID:** 1719417

**Cheating detected:** Yes

```diff
- читерили, да?
```

## Task 3

### Subtask 1

Дать определение понятию “класс” в java. Из чего он состоит?

```
Классы в Java - это ...
Класс — это шаблон, описывающий структуру объектов: их данные (поля) и поведение (методы).
Он определяет, какие свойства есть у объекта и какие действия он может выполнять.
Класс также содержит конструкторы, внутренние классы, статические элементы и другую служебную информацию.

Класс — это тип данных, а объект — экземпляр этого типа. Физически объект хранится в куче (heap),
где выделяется память под его поля. Методы класса хранятся в Metaspace и общие для всех объектов этого класса.

Класс является основой ООП. Он моделирует сущности реального мира и позволяет создавать множество объектов,
каждый со своим состоянием, но с одинаковым поведением.

```

### Subtask 2

Какое отношение между классами и типами данных? Коротко о “физической сути” класса как разметки памяти.

```
класс это пользовательский тип данных. как int,double float -встроенные типы   как класс такой же тип только созданный тобой когда ты создаёшь класс фактически создаёшь новый тип,по которому  потом будешь создавать перменный объекты
то есть класс это чертёж а объект это выделенный кусок памяти по этому чертежу
например чертёж автомобиля Объект= конкретная машина,занимающая место в реальной мире
```

```diff
+ за этот ответ + балл. Спасибо что слушаете лекции.
```

### Subtask 3

Дать определение понятию “объект” в java. Дать определение инициализации объекта.

```
Объект — это конкретный экземпляр класса, который существует в памяти и содержит реальные значения полей.
Когда мы вызываем new, JVM выделяет память в куче, инициализирует поля значениями по умолчанию
и вызывает конструктор, который присваивает им начальные значения.Процесс инициализации включает:
1) выделение памяти,
2) установка стандартных значений (числа = 0, boolean = false, ссылки = null),
3) вызов конструктора.

Инициализация гарантирует, что объект всегда находится в корректном состоянии и что программа не работает
с «мусорными» данными. После этого объект может выполнять методы и изменять своё состояние.
```

### Subtask 4

Дано описание предмета из реального мира.<br>
Необходимо реализовать класс <code>CoffeeMachine</code>.<br><br>

<b>Описание класса CoffeeMachine</b><br><br>

<b>Поля</b><br>
<ul>
	<li><code>brand</code> — бренд кофемашины (строка)</li>
	<li><code>waterLevel</code> — текущий уровень воды в миллилитрах (int)</li>
	<li><code>beansLevel</code> — уровень кофейных зёрен в граммах (int)</li>
	<li><code>cupsMade</code> — количество приготовленных чашек кофе (int)</li>
</ul>

<b>Конструктор</b><br>
Принимает:<br>
<ul>
	<li>бренд</li>
	<li>стартовый уровень воды</li>
	<li>стартовый уровень зёрен</li>
</ul>

<b>Методы</b><br><br>

<code>makeCoffee(int waterNeeded, int beansNeeded)</code><br>
Готовит кофе, если хватает ресурсов.<br>
Уменьшает уровень воды и зёрен, увеличивает <code>cupsMade</code>.<br>
Выводит сообщение об успешном приготовлении или об ошибке.<br><br>

<code>refillWater(int amount)</code><br>
Добавляет воду.<br><br>

<code>refillBeans(int amount)</code><br>
Добавляет зёрна.<br><br>

<code>printStatus()</code><br>
Выводит текущие уровни воды, зёрен и количество приготовленных чашек.<br><br>

<b>Разрешено изменять только класс <code>CoffeeMachine</code>.</b>


```java
class CoffeeMachine {
private String brand;
private int waterLevel;
private int cupsMade;
public CoffeeMachine ( String brand, int waterLevel, int beansLevel){
	this.brand = brand;
	this.waterLevel =waterLevel;
	this.beanslevel = beansLevel;
	this.cupsMade = 0;
}
public void makeCoffe(int waterNeeded, int beansNeeded){
	if (waterLevel >= waterNeeded && beansLevel >= beansNeeded){
		waterLevel -= waterNeeded;
		waterLevel -= beansLevel;
		 cupsMade++;
		 System.out.println("кофе приготовлен");

	} else {
		System.out.println("недостаточно ресов для приготовлениякофе.");
	}
} public void refilwater(int amount){
	waterLevel += amout;
	System.out.println("вода добавлена:"+ amount);
}
public  void refillBeans(int amount){
	beansLevel += amount;
	System.out.println("зёрна добавлены"+ amount);
}
 public void printStatus(){
 	System.out.println("Бренд"+ brand);
 	System.out.println("вода:" +waterLevel + "ml");
 	System.out.println("Зерна: " +beansLevel + "gramm");
 	System.out.println("приготовлено чашек"+ cupsMade);
 }
}

public class Main {
	public static void main(String[] args) {
		CoffeeMachine machine = new CoffeeMachine("DeLonghi", 1000, 200);

		machine.printStatus();
		machine.makeCoffee(150, 15);
		machine.makeCoffee(500, 50);

		System.out.println();

		machine.refillWater(300);
		machine.refillBeans(40);

		machine.printStatus();
	}
}




```

**Output:**

```
Compilation error:
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:8: error: cannot find symbol
	this.beanslevel = beansLevel;
	    ^
  symbol: variable beanslevel
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:12: error: cannot find symbol
	if (waterLevel >= waterNeeded && beansLevel >= beansNeeded){
	                                 ^
  symbol:   variable beansLevel
  location: class CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:14: error: cannot find symbol
		waterLevel -= beansLevel;
		              ^
  symbol:   variable beansLevel
  location: class CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:22: error: cannot find symbol
	waterLevel += amout;
	              ^
  symbol:   variable amout
  location: class CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:26: error: cannot find symbol
	beansLevel += amount;
	^
  symbol:   variable beansLevel
  location: class CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:32: error: cannot find symbol
 	System.out.println("?????: " +beansLevel + "gramm");
 	                              ^
  symbol:   variable beansLevel
  location: class CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:42: error: cannot find symbol
		machine.makeCoffee(150, 15);
		       ^
  symbol:   method makeCoffee(int,int)
  location: variable machine of type CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:43: error: cannot find symbol
		machine.makeCoffee(500, 50);
		       ^
  symbol:   method makeCoffee(int,int)
  location: variable machine of type CoffeeMachine
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:47: error: cannot find symbol
		machine.refillWater(300);
		       ^
  symbol:   method refillWater(int)
  location: variable machine of type CoffeeMachine
9 errors

```
```diff
-много ошибок.
+что же вы так? не могли поправить чтобы оно компилилось?
@@@ 2/4
```


## Task 8

### Subtask 1

Определение наследования в Java

```
Наследование классов в Java - это Наследование, что наследуется, что нет, final классы
Наследование позволяет классу-потомку получить методы и поля родителя. например protected
```

### Subtask 2

Перечислить все наследуемые конструкции класса

```
Наследуются:	все public, protected поля и методы,	package-private элементы (если в том же пакете),
абстрактные методы,
конкретные методы,	статические методы и поля (формально доступны, но не переопределяются).
```

### Subtask 3

Перечислить все НЕ наследуемы элементы класса

```
не наследуется:	конструкторы,	private члены,	блоки инициализации,	методы final нельзя переопределять.
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


        }

        System.out.println(rc.priority);
    }
}

class Component {
	public void Component (){
		Component[] components = { rc, pc };
    int Components[] rc = {type boolean, int, float};
        for (Component c : components) {
            c.disable();
            c.update();
            System.out.println();
}            id = id;
        tenabled = enabled;
        tpriority = priority;
        damping = damping;

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
Compilation error:
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:14: error: <identifier> expected
        System.out.println(rc.priority);
                          ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:14: error: <identifier> expected
        System.out.println(rc.priority);
                                      ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:16: error: class, interface, enum, or record expected
}
^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: ';' expected
    int Components[] rc = {type boolean, int, float};
                    ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: illegal start of expression
    int Components[] rc = {type boolean, int, float};
                          ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: not a statement
    int Components[] rc = {type boolean, int, float};
                           ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: ';' expected
    int Components[] rc = {type boolean, int, float};
                               ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: not a statement
    int Components[] rc = {type boolean, int, float};
                                ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: ';' expected
    int Components[] rc = {type boolean, int, float};
                                       ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: not a statement
    int Components[] rc = {type boolean, int, float};
                                         ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: ';' expected
    int Components[] rc = {type boolean, int, float};
                                            ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: not a statement
    int Components[] rc = {type boolean, int, float};
                                              ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:21: error: ';' expected
    int Components[] rc = {type boolean, int, float};
                                                   ^
C:\Users\GTU-512B-514\Downloads\exam\.\Main.java:97: error: reached end of file while parsing
}
 ^
14 errors

```


## Task 2

### Subtask 1

Абстракция. Дать одно из определений из лекций.

```
Абстракция - это
Абстракция - принцип, заключающийся в выделении главных характеристик объекта и игнорировании мелких деталей.
В программировании абстракция помогает уменьшать сложность системы, делить её на логические компоненты и
скрывать внутреннюю реализацию классов.



Основная мотивация использования абстракции - упрощение поддержки кода, уменьшение количества ошибок,
повышение модульности и возможность менять реализацию без изменения внешнего интерфейса классов.
```

### Subtask 2

Кратко опишите, какая мотивация использовать абстракцию и абстрактное мышление в программировании?

```
Она позволяет программисту работать с «идеей» объекта, не думая о сложных внутренних процессах.
Например, мы пользуемся телефоном, не зная, как работает процессор или графический чип.
В Java абстракция реализуется через абстрактные классы, интерфейсы и хорошо спроектированные иерархии.
```

### Subtask 3

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
