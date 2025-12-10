```diff
@@@ финалочка:
- 23/30

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠉⠉⠉⠉⠉⠙⠓⢦⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⢠⣤⡶⠶⠶⠶⠶⣤⣄⠀⠹⣧⡀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠀⠸⣿⣦⣄⣀⣠⣤⣤⡿⠀⠀⠘⣧
⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⢹⡄
⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇
⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇
⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⢠⡶⠒⠒⠒⠒⠲⣦⡀⠀⠀⠀⠀⠀⣿
⠀⣀⣠⣄⣀⣼⡇⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⡇
⠸⣏⡀⠀⠀⠈⠀⠀⠀⣀⣼⡇⠀⠀⣀⣀⣠⣼⠃⠀⠀⠀⠀⠀⡏
⠀⠈⠛⠛⠒⠒⠒⠛⠛⠉⠁⠀⠀⣾⠉⠀⠀⠀⠀⠀⠀⠀⢀⣰⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠒⠒⠚⠛⠉⠉
```

# Java Mid-Term Exam

**Student:** მიხაილოვა ვიოლეტტა

**Student ID:** 1376288

**Cheating detected:** No

## Task 3

### Subtask 1

Дать определение понятию “класс” в java. Из чего он состоит?

```
Классы в Java - это шаблон, по которому создаются объекты. Это пользоваительский тип данных, объеденяющий состояние и поведение объектов
Классы состоят из: (3 пункта)
1. поля бывают приватные (доступны только внутри класса)и публичные.
2. методы могут принимать параметры, а также могут возвращать значения.
3. конструкторы, имя конструктора равняется имя класса. Не имеет типа возвращаемого значения.
```

### Subtask 2

Какое отношение между классами и типами данных? Коротко о “физической сути” класса как разметки памяти.

```
Класс Джава это описание того, как будут размечены и интепретированы данные памяти. Тип данных- говорит сколько памяти и какой структуры нужно. Класс- задает разметку памяти объекта. Объект- это конкретный часток памяти, созданный по этой разметке.
```

### Subtask 3

Дать определение понятию “объект” в java. Дать определение инициализации объекта.

```
Объекта Джава- это конкретный экземпляр класса, созданный в памяти, который имеет свое состояние в виде значений полей и проведение, определяемое методами класса.Объект создается в динамической памяти, а доступ к нему осуществляется через ссылку.
Инициализация объекта- это процесс присвоения начальных значений его полям в момент создания. Она выполняется с помощью конструктора, блоков инициализации и значений по умолчанию.Создание объекта и его инициализация происходят одновременно при использовании оператора "новый, но логиеский это 2 разных этапа: сначала выделяется память под объект, затем его поля наполнются начальными значениями.
```

``` diff
- ну ок
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
private String model;
private int water;
private int drinks;
private int cupsMade;
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

```diff
- ну, что-то попытались. 1/4
```

**Output:**

```

```


## Task 8

### Subtask 1

Определение наследования в Java

```
Наследование классов в Java - это механизм объектно-ориентированного программирования, при котором один класс (подкласс) получает свойства и методы другого класса (суперклсса), расширяя или переопределяя его функциональность. Наследование позволяет повторно ипользовать код, создовать иерархии классов, расширять поведение существующих классов, реализовывать принцип полиморфизма.
```

### Subtask 2

Перечислить все наследуемые конструкции класса

```
Подкласс автоматически получает от родительского класса: поля, методы, статические методы, вложенные классы, инициализаторы.
```

### Subtask 3

Перечислить все НЕ наследуемы элементы класса

```
Не наследуется в джава: конструкторы, приватные поля и приватные методы, финальные методы, локальные переменные методы.
```

а вот и ошибка. методы файнал наследуются, но их нельзя переопределять.



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

```diff
- нет попытки решения. жаль. 0/4
- у вас же сданы лабы, вам надо было сделать только 2 задачи выше. Ну ладно. Надеюсь вы что-то запомнили.
```

## Task 2

### Subtask 1

Абстракция. Дать одно из определений из лекций.

```
Абстракция - это процесс выделения существенных свойств объекта и скрытия несущественных деталей, позволяющий работать с объектом на уровне его интерфейса, не вдаваясь во внутреннюю реализацию.
```

### Subtask 2

Кратко опишите, какая мотивация использовать абстракцию и абстрактное мышление в программировании?

```
Мотивация использования абстракции и абстрактного мышления в программиовании заключается в том, чтобы: сосредаточиться на сути задачи, выделяя только важные свойства объекта и поведении скрывая детали реализации. Повысить повторное испоьзование кода, создова общий интерфейс для разных реализаций. Облегчить сопровождение и изменение программы, так как изменение в реализации не влияют на использование объекта через абстракцию. Снизить сложность системы, позволяя мыслить в высокоуровневых концепциях, а не о каждой мелко детали.
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
