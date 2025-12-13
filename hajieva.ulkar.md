``` diff
- 1 практики нет.
- в ответах - неточности + 1 вопрос вообще не тот %)
- Итог: 23/30.
```

# Java Mid-Term Exam

**Student:** ჰაჯიიევა ულკარ

**Student ID:** 1303006

**Cheating detected:** Yes

## Task 3

### Subtask 1

Дать определение понятию “класс” в java. Из чего он состоит?

```
Классы в Java - это шаблоны, по которым создаются объекты. Класс описывает какие данные будут у объекта(поля), что он может делать(методы) и как создавать экземпляры(конструкторы)
Классы состоят из: Полей, переменные которые хранят состояние объекта. Методы: функции, которые определяют поведение объекта. Конструкторы, специальные методы для создания объектов класса. Блоки инициализации, статические и нестатические блоки. Вложенные классы и интерфейсы, классы, объявления внутри другого класса
```

### Subtask 2

Какое отношение между классами и типами данных? Коротко о “физической сути” класса как разметки памяти.

```
Класс - это ссылочны тип данных:																Классы в Java в отличие от примитивных типов(int, boolen) являются ссылочными типами данных						Создавая класс, вы фактически определяете свой собственный новый тип данных, который можно использовать для объявления переменных и полей															Класс- это логическая сущность. Он существует как шаблон и набор инструкций для JVM. Он не занимает памяти для хранения конкретных данных (значений полей). Он лишь определяет,какого размера должен быть объект и какие поля и методы он должен содержать
```

```diff
- а это что? копипаста из ГПТ? выглядит крайне подозрительно
```

### Subtask 3

Дать определение понятию “объект” в java. Дать определение инициализации объекта.

```
Объект-это физическая сущность, создаваемая оператором. При создании объекта JVM выделяет фактическую область памяти в соответствии с "разметкой" класса. В этой области памяти хранятся конкретные значения полей для этого уникального экземпляра
```
```diff
- каким оператором?
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
	private int beanLevel;
	private int cupsMade;

	public CoffeeMachine(String brand, int initialWater, int initialBeans) {
		this.brand = brand;
		this.waterLevel = initialWater;
		this.beanLevel = initialBeans;
		this.cupsMade = 0;
		System.out.println("Кофемашина " + this.brand + " готова к работе");
	}

	public void makeCoffee(int waterNeeded, int beansNeeded){
		System.out.println("Попытка приготовить кофе ( Вода: " + waterNeeded + "млб Зерна: " + beansNeeded + "г) ");
		if (this.waterLevel >= waterNeeded && this.beanLevel >= beansNeeded){
			this.waterLevel -= waterNeeded;
			this.beanLevel -= beansNeeded;
			this.cupsMade++;
			System.out.println("Чашка кофе приготовлена!");
		}else{
			System.out.println("Ошибка: недостаточно ресурсов для приготовления кофе!");
			if(this.waterLevel < waterNeeded) {
				System.out.println("Не хватает воды, требуется" + waterNeeded + "ml, в наличии " + this.waterLevel + "ml");
			}
			if(this.beanLevel < beansNeeded) {
				System.out.println("Не хватает зерен, требуется" + beansNeeded + "г, в наличии " + this.beanLevel + "ml");
			}
		}
	}

	public void refillWater(int amount) {
		this.waterLevel += amount;
		System.out.println("Добавлено" + amount + "ml. Текущий уровень воды: " + this.waterLevel + "мл");
	}

	public void refillBeans(int amount) {
		this.beanLevel += amount;
		System.out.println("Добавлено" + amount + "g. Текущий уровень зёрен: " + this.beanLevel + "мл");
	}

	public void printStatus(){
		System.out.println("\n  Статус " + this.brand);
		System.out.println(" Уровень воды: " + this.waterLevel + " мл");
		System.out.println(" Уровень зёрен: " + this.beanLevel + " г");
		System.out.println(" Всего чашек приготовлено: " + this.cupsMade);
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
���������� DeLonghi ������ � ������

  ������ DeLonghi
 ������� ����: 1000 ��
 ������� ����: 200 �
 ����� ����� ������������: 0
������� ����������� ���� ( ����: 150��� �����: 15�)
����� ���� ������������!
������� ����������� ���� ( ����: 500��� �����: 50�)
����� ���� ������������!

���������300ml. ������� ������� ����: 650��
���������40g. ������� ������� ����: 175��

  ������ DeLonghi
 ������� ����: 650 ��
 ������� ����: 175 �
 ����� ����� ������������: 2

```

```diff
- ооо, ну можете же накодить !! а говорили!!!
```


## Task 8

### Subtask 1

Определение наследования в Java

```
Наследование классов в Java - это когда один класс (дочерний) "берёт" поля и методы другого класса родительского чтобы не писать заново
```

### Subtask 2

Перечислить все наследуемые конструкции класса

```
public - Доступен везде. protected - доступен в том же пакете во всех подклассах(наследника). Package private - доступен только внутри того же пакета
```
```diff
-а private?
- подождите, а вы вопрос читали? что наследуется в классе, а вы мне про модификаторы доступа отвечаете...
```

### Subtask 3

Перечислить все НЕ наследуемы элементы класса

```
В Java не наследуются:
1. Конструкторы
2. private члены
3. статические члены
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
	public static void
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
- тут без попытки.
```

```diff
+ ВАМ НУЖНО БЫЛО ВЫБРАТЬ 2 ЗАДАЧИ ИЗ 3.

:)

Третья засчитывается автоматом. Ну если вам интересно было поупражняться в наборе текста на клавиатуре...
```

## Task 2

### Subtask 1

Абстракция. Дать одно из определений из лекций.

```
Абстракция - это когда мы убираем детали, которые не важны на данном этапе и оставляем только то, что нужно сейчас
```

### Subtask 2

Кратко опишите, какая мотивация использовать абстракцию и абстрактное мышление в программировании?

```
Это помогает уменьшить сложность программы и концентрироваться на сути
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
