<font color="red"> OБЩАЯ ОЦЕНКА: 25/30 баллов</font>

# Java Mid-Term Exam

**Student:** აბრამიანი ალექსანდრე

**Student ID:** 1691682

**Cheating detected:** No

## Task 12 (9 points)

### Subtask 1

Что такое интерфейс в Java? Могут ли в интерфейсе быть методы с реализацией? Зачем нужны интерфейсы, не достаточно ли абстрактных и обычных классов?

```
1.Интерфейс  — это специальный тип в Java, который задаёт контракт: набор методов, которые должен реализовать класс.
Интерфейс описывает что должен уметь объект, но не обязательно как он это делает.
2.Да,могут быть методы с реализацией (static, default, private) начиная с java 9
3.Интерфейсы решают задачи, которые классы решить не могут:
Множественное наследование поведения;Интерфейс задаёт роль / поведение, а не структуру;Интерфейсы позволяют писать код на основе абстракций, а не конкретных классов.


```
<font color="red"> ОЦЕНЕНО: **5 баллов**</font>

### Subtask 2

Как наследуются методы интерфейса? Как наследовать интерфейс (ключевое слово) и возможно ли наследование нескольких интерфейсов одним классом?

```
1.Когда класс реализует интерфейс,он наследует только сигнатуры методов интерфейса
и обязан реализовать все его абстрактные методы.Если интерфейс содержит default-метод, класс не обязан его переопределять
2.Интерфейс наследуется от другого интерфейса с помощью ключевого слова extends
3.Да, интерфейс может наследовать несколько интерфейсов.
```

<font color="red"> ОЦЕНЕНО: **4 баллов**</font> последний вопрос - неверно. Вчитайтесь: "возможно ли наследование нескольких интерфейсов одним классом"

## Task 9

### Subtask 1

Что такое final классы и какая их связь с наследованием?

```
Ключевое слово final, применённое к классу, означает ,что класс нельзя наследовать.
Используется, когда автор класса не хочет, чтобы кто-либо мог изменить его логику через наследование.


```


<font color="red"> ОЦЕНЕНО: **1 баллов**</font>

### Subtask 2

Разрешено ли множественное наследование в Java и почему?

```
Множественное наследование запрещено,чтобы избежать проблемы ромбовидного наследования и усложнения иерархии,но разрешенно множественное наследование интерфейсов
```

<font color="red"> ОЦЕНЕНО: **2 баллов**</font>
### Subtask 3

Для чего используется ключевое слово super? Как наследуются конструкторы родительских классов в дочерних?

```
super - это специальное ключевое слово в дочерних классах  для обращения к родительским классам.
Конструкторы не наследуются.
```

<font color="red"> ОЦЕНЕНО: **2 баллов**</font> "к родительским классам" что? куда? Ну да, с родителями нужно только супер - только уважительно.
ну и тут же в вопросе подсказка: я ожидал что вы напишете про конструкторы не наследуются, НО можно super.Parent()....
но ладно.

### Subtask 4

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
	protected boolean checkPassword(String hash) {
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
	protected boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	// TODO: указать модификатор доступа
	private int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);
		System.out.println(admin.getUsername());

		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
	}
}

```
```diff
	private String username;

	// TODO: указать модификатор доступа
	private String passwordHash;

- это не private
```

<font color="red"> ОЦЕНЕНО: **1 баллов**</font> а методы и поля паблик повызывать? Ну за protected плюс однозначно, хотя он тут себя сомнительно оправдывает

**Output:**

```
C:\Users\GTU-Student\Downloads\exam\.\Main.java: root

```


## Task 5

### Subtask 1

Дать определение “поле класса”

```
Поле класса - это переменная объявленная внутри класс, которая хранит данные объекта или самого класса
```

<font color="red"> ОЦЕНЕНО: **2 баллов**</font> Вот тут я начал подозревать ЧатГПТ, либо вы хорошо готовились...
### Subtask 2

Дать определение “метод класса”

```
Метод класса - это функция описанная внутри класса,которая определяет поведение объектов класса или самого класса
```

<font color="red"> ОЦЕНЕНО: **2 баллов**</font>
### Subtask 3

Дать определение "Сигнатура метода" и её составляющие

```
Сигнатура метода класса в Java - это уникальное описание метода по которому кампилятор отличает один метод от другого.
Включает в себя имя метода,список типов параметров.
```

<font color="red"> ОЦЕНЕНО: **2/2 баллов**</font> это лично моя фишка. Я ввожу в сигнатуру метода возвращаемый тип, модификатор доступа и throws. Но уж как есть.
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
    String brand;
    int waterlevel;
    int beanslevel;
    int cups;

    public CoffeeMachine(String brand, int waterlevel, int beanslevel) {
        this.brand = brand;
        this.waterlevel = waterlevel;
        this.beanslevel = beanslevel;
        this.cups = 0;
    }

    public void makeCoffee(int waterNeeded, int beansNeeded) {
        if (waterlevel >= waterNeeded && beanslevel >= beansNeeded) {
            waterlevel -= waterNeeded;
            beanslevel -= beansNeeded;
            cups++;
            System.out.println("Кофе приготовлен!");
        } else {
            System.out.println("Ошибка! Недостаточно ресурсов!");
        }
    }

    public void refillWater(int amount) {
        waterlevel += amount;
    }

    public void refillBeans(int amount) {
        beanslevel += amount;
    }

    public void printStatus() {
        System.out.println("Бренд: " + brand);
        System.out.println("Зёрна: " + beanslevel + " гр");
        System.out.println("Вода: " + waterlevel + " мл");
        System.out.println("Приготовлено чашек: " + cups);
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
C:\Users\GTU-Student\Downloads\exam\.\Main.java:
Бренд: DeLonghi
Зёрна: 200 гр
Вода: 1000 мл
Приготовлено чашек: 0
Кофе приготовлен!
Кофе приготовлен!

Бренд: DeLonghi
Зёрна: 175 гр
Вода: 650 мл
Приготовлено чашек: 2
```


<font color="red"> ОЦЕНЕНО: **4/4 баллов**</font> Ну что, не к чему придраться, а я очень старался.
