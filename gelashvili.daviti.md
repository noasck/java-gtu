```diff
- есть немного неточностей и в последней задаче есть нюансы (не до конца написали методы)
+ 27/30
                                   (  )/
                                    )(/
                 ________________  ( /)
                ()__)____________)))))

___    A
| |   {*}
| |  __V__
|_|o_|%%%|0_
   |       |
   |       |
   |_______|


```

# Java Mid-Term Exam

**Student:** გელაშვილი დავითი

**Student ID:** 1416432

**Cheating detected:** No

## Task 3

### Subtask 1

Дать определение понятию “класс” в java. Из чего он состоит?

```
Классы в Java - это пользовательский тип данных
Классы состоят из: (3 пункта)
- поля
- методы
- конструктор
```

### Subtask 2

Какое отношение между классами и типами данных? Коротко о “физической сути” класса как разметки памяти.

```
Классы позволяют создавать собственный тип данных для реализации объекто-ориентированной парадигмы.
```

### Subtask 3

Дать определение понятию “объект” в java. Дать определение инициализации объекта.

```
Объект - это инициализированный экземпляр класса. Создается ключевым словом new.
Инициализаци - это выделение области в памяти для объекта и присваевание начальных значений.
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
	public String brand;
	public int waterLevel;
	public int beansLevel;
	public int cupsMade;

	public void makeCoffee(int waterNeeded, int beansNeeded) {
		if (waterLevel >= waterNeeded && beansLevel >= beansNeeded) {

			waterLevel -= waterNeeded;
			beansLevel -= beansNeeded;
			++cupsMade;
			System.out.println("Done!");
		} else {
			System.out.println("Need more water or beans");
		}
	}

	public void refillWater (int amount) {
		waterLevel += amount;
		System.out.println("Current Water Level: " + waterLevel);
	}

	public void refillBeans (int amount) {
		beansLevel += amount;
		System.out.println("Current Beans Level: " + beansLevel);
	}

	public void printStatus() {
		System.out.println("Water Level: " + waterLevel);
		System.out.println("Beans Level: " + beansLevel);
		System.out.println("Cups of coffe made: " + cupsMade);
	}

	public CoffeeMachine (String brand, int waterLevel, int beansLevel) {
		this.brand = brand;
		this.waterLevel = waterLevel;
		this.beansLevel = beansLevel;
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
Water Level: 1000
Beans Level: 200
Cups of coffe made: 0
Done!
Done!

Current Water Level: 650
Current Beans Level: 175
Water Level: 650
Beans Level: 175
Cups of coffe made: 2

```


## Task 8

### Subtask 1

Определение наследования в Java

```
Наследование классов в Java - это ...
```

### Subtask 2

Перечислить все наследуемые конструкции класса

```

```

### Subtask 3

Перечислить все НЕ наследуемы элементы класса

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


## Task 2

### Subtask 1

Абстракция. Дать одно из определений из лекций.

```
Абстракция - это намеренное отбрасывание подробностей для реализации общего поведения.
```

### Subtask 2

Кратко опишите, какая мотивация использовать абстракцию и абстрактное мышление в программировании?

```
Абстракции позволяют проще описывать сложные системы, отбрасывая частные случаи и поиска общего.
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
	public String name;
	public double weight;
	public int durability;

	public void repair(int amount){
		durability += amount;
		System.out.println(name + " repaired by " + amount + ". Durability=" + durability);
	}

	public void use() {

	}
}

class Sword extends Item {
	public int damage;

	public Sword(String name, double weight, int durability, int damage) {
		super();
		this.name = name;
		this.weight = weight;
		this.durability = durability;
		this.damage = damage;
	}

	public void use() {
		System.out.println(name + " slashes for " + damage + " damage!");
		durability -= 1;
	}
}

class Staff extends Item {
	public int manaBonus;

	public Staff(String name, double weight, int durability, int manaBonus) {
		super();
		this.name = name;
		this.weight = weight;
		this.durability = durability;
		this.manaBonus = manaBonus;
	}

	public void use() {
		System.out.println(name + " channels magic with +" + manaBonus + " mana!");
		durability -= 1;
	}
}


```

**Output:**

```
Excalibur slashes for 25 damage!
Elder Staff channels magic with +40 mana!

Excalibur repaired by 5. Durability=104
Excalibur slashes for 25 damage!

Elder Staff repaired by 5. Durability=124
Elder Staff channels magic with +40 mana!

103

```
