
```diff
- суммарно 19/30

             _     ______
            / | _''      ``\_
           / //'___  \       \_
           |_  /###\ ``-__     \__*
             /|#####|__  ``-_/\   |
            /  \###//ZZ`-__  \/  /
            |/'---/_;ZZZZ  `-_ `|
            . ZZZ @  ;;; @  ;Z\ |
             \__      .     ;Z .
              ZZ\#         #/_'
               ;;`-_ --- _-`;
              ######|   |#####
             ####  ############
             /`##############\
            / zZZZ      Z#### |
           /ZZZ_`|       ZZz  \
          zz/$$/ |#      #ZZ   \
        zz__$$/  |        |Zz   \
       z/###`-   |#      #|zZ   \
      z/######| _|        |zZZ   \
     z/#######// | _ . _  |\ZZz  |
    z/#######/ |_`- \_/ -`_/;Zz  |
    z|__####/ /;/`'____ '`..\ZZZ |
    z###`__/ /;/,,,|--/......\zZ |
   z|###|   /;/,,,,|..|../ `-.\ZZ|
   z ||||  /;/,,,,,|..|./ ## `|zZz
  Zz \\\  /;/,,,,,,|..|/ ####  |ZZz
 ZZ   -_  |;|,,,,,,|..|   ###  |zZz
 ZZ    ;| \;\,,,,,,|..|  ## #  ||ZZ
zZZ     | \`_\*\,__.--/  ####  ||ZZZ
zZ      |  \ *  *  |__ _##  ##_/| ZZ
        ;\--. _____/ '\_\____// |/zz
            |#####|`  |#\_  _/ ;
            |#####|   |###--#|
            |#####|   |######|
           |######|   |######|
           |_---_|    |#_--_#|
           /#####|    |/####\|
          |######|    |######\
          `------`    `-------`
          `------`    `-------`
```

# Java Mid-Term Exam

**Student:** ბირიუკოვიჩ არსენი

**Student ID:** 1605343

**Cheating detected:** Yes
```diff
- читерите!
```
## Task 1

### Subtask 1

Дать определение JVM, JRE, JDK. Расшифровка каждой аббревиатуры, назначение и взаимосвязь.

```
JRE - Это JVM плюс набор стандартных коментариев
JDK - Набор разработки и компилятор
JVM - Виртуальная машина для постобработки
```

```diff
- каких таких комментариев?
```
### Subtask 2

Проблема платформозависимости: почему нужно компилировать код по-разному для каждой операционной системы и какие неудобства с этим связаны?

```
не знаю, но для решения этого придумали jvm
```

```diff
- мда
```
### Subtask 3

Мотивация создания JVM и диаграмма процесса компиляции и исполнения: машинный код, исходный код, байт-код.

```
Позволяет скомпилировать код почти для каждой операционной сиситемы
компилятор-создаёт машинный код
исходный-JVM-байт код
```

```diff
- ок, что-то близко.
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
	int filamentLevel;
	int powerLevel;
	int objectsPrinted;

	public void Printer3D(String initialModel, int initialFilamentLevel, int initialPowerLevel){
		String model = initialModel;
		int filamentLevel = initialFilamentLevel;
		int powerLevel = initialPowerLevel;
	}

	public void PaintObject(int filamentNeeded, int powerNeeded){
		if(filamentNeeded <= filamentLevel && powerNeeded <= powerLevel ){
				powerLevel -= powerNeeded;
				filamentLevel -= filamentNeeded;
				++objectsPrinted;
				System.out.println("Print object");
			}else{
				System.out.println("Needed power or filament");
				}
	}

	public void refillFilament(int amount){
			filamentLevel += amount;
		}

	public void recharge(int amount){
			 powerLevel += amount;
		}

		public void printStatus(){
			 System.out.printf("Now level Filament %d \n And level charge %d \n and countPrint %d");
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
C:\Users\GTU-Student\Desktop\java\.\Main.java:40: error: constructor Printer3D in class Printer3D cannot be applied to given types;
		Printer3D printer = new Printer3D("Creality Ender 3", 500, 80);
		                    ^
  required: no arguments
  found:    String,int,int
  reason: actual and formal argument lists differ in length
C:\Users\GTU-Student\Desktop\java\.\Main.java:43: error: cannot find symbol
		printer.printObject(50, 10);
		       ^
  symbol:   method printObject(int,int)
  location: variable printer of type Printer3D
C:\Users\GTU-Student\Desktop\java\.\Main.java:44: error: cannot find symbol
		printer.printObject(200, 40);
		       ^
  symbol:   method printObject(int,int)
  location: variable printer of type Printer3D
3 errors

```

```diff
- не компилится. Ну хоть начали делать.
```

## Task 7

### Subtask 1

Статические поля - определение и их свойства. Статические методы - определение и их свойства.

```
Статическое поле - это поле которое не привязанно к объекту класса
Статический метод - это поле которое не привязанно к массиву класса
```

```diff
- метод - это поле? Поле комплексных чисел может???
```
### Subtask 2

Зачем нужны статические члены класса? Приведите пример, где это может понадобиться.

```
Как так в java нету глобальных переменных статические пооля несут функции константы
```

```diff
- воо, вот это конечно хороший ответ. Не только для этого, но да. Статика компенсирует global state.
```
### Subtask 3

Статические импорты - что это и зачем нужно

```
Они упрощают доступ
```

```diff
- доступ куда? вам то понятно, что вы написали, а мне же тоже нужно знать, что за доступ, куда.
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

```json
{
  "-1": "1",
  "1000": "JRE - Это JVM плюс набор стандартных коментариев\nJDK - Набор разработки и компилятор \nJVM - Виртуальная машина для постобработки",
  "1001": "не знаю, но для решения этого придумали jvm",
  "1002": "Позволяет скомпилировать код почти для каждой операционной сиситемы\nкомпилятор-создаёт машинный код\nисходный-JVM-байт код",
  "1003": "class Printer3D {\n\tString model;\n\tint filamentLevel;\n\tint powerLevel;\n\tint objectsPrinted;\n\n\tpublic void Printer3D(String initialModel, int initialFilamentLevel, int initialPowerLevel){\n\t\tString model \u003d initialModel;\n\t\tint filamentLevel \u003d initialFilamentLevel;\n\t\tint powerLevel \u003d initialPowerLevel;\n\t}\n\n\tpublic void PaintObject(int filamentNeeded, int powerNeeded){\n\t\tif(filamentNeeded \u003c\u003d filamentLevel \u0026\u0026 powerNeeded \u003c\u003d powerLevel ){\n\t\t\t\tpowerLevel -\u003d powerNeeded;\n\t\t\t\tfilamentLevel -\u003d filamentNeeded;\n\t\t\t\t++objectsPrinted;\n\t\t\t\tSystem.out.println(\"Print object\");\n\t\t\t}else{\n\t\t\t\tSystem.out.println(\"Needed power or filament\");\n\t\t\t\t}\n\t}\n\n\tpublic void refillFilament(int amount){\n\t\t\tfilamentLevel +\u003d amount;\n\t\t}\n\t\n\tpublic void recharge(int amount){\n\t\t\t powerLevel +\u003d amount;\n\t\t}\n\n\t\tpublic void printStatus(){\n\t\t\t System.out.printf(\"Now level Filament %d \\n And level charge %d \\n and countPrint %d\");\n\t}\n}\n\npublic class Main {\n\tpublic static void main(String[] args) {\n\t\tPrinter3D printer \u003d new Printer3D(\"Creality Ender 3\", 500, 80);\n\n\t\tprinter.printStatus();\n\t\tprinter.printObject(50, 10);\n\t\tprinter.printObject(200, 40);\n\t\t\n\t\tSystem.out.println();\n\n\t\tprinter.refillFilament(100);\n\t\tprinter.recharge(20);\n\t\t\n\t\tprinter.printStatus();\n\t}\n}\n",
  "7000": "Статическое поле - это поле которое не привязанно к объекту класса\nСтатический метод - это поле которое не привязанно к массиву класса",
  "11000": "Абстрактный класс - это содержат такие-же методы, обязательны для переопределения дочерними классами, у обстрактного класса нельзя создать объект\nАбстрактный метод - это\tпереопределения дочерними классами.",
  "7001": "Как так в java нету глобальных переменных статические пооля несут функции константы",
  "11001": "что бы обобщить различные методы в дркгих классах",
  "7002": "Они упрощают доступ ",
  "11002": "форсирую реализацию через потомков",
  "7003": "class LogHelper {\n\n}\n\npublic class Main {\n\tpublic static void main(String[] args) {\n\t\tLogHelper.configure(2, \"APP\");\n\n\t\tLogHelper.printStatus();\n\t\tLogHelper.log(1, \"Критическая ошибка\");\n\t\tLogHelper.log(3, \"Отладочная информация\");\n\n\t\tSystem.out.println();\n\n\t\tLogHelper.setLevel(3);\n\t\tLogHelper.setPrefix(\"CORE\");\n\n\t\tLogHelper.printStatus();\n\t\tLogHelper.log(2, \"warning\");\n\t}\n}\n",
  "11003": "public class Main {\n\tpublic static void main(String[] args) {\n\t\tSword sword \u003d new Sword(\"Excalibur\", 5.0, 100, 25);\n\t\tStaff staff \u003d new Staff(\"Elder Staff\", 3.0, 120, 40);\n\n\t\tsword.use();\n\t\tstaff.use();\n\n\t\tSystem.out.println();\n\n\t\tItem[] items \u003d { sword, staff };\n\n\t\tfor (Item it : items) {\n\t\t\tit.repair(5);\n\t\t\tit.use();\n\t\t\tSystem.out.println();\n\t\t}\n\n\t\tSystem.out.println(sword.durability);\n\t}\n}\n\nclass Item {\n}\n\nclass Sword extends Item {\n\tpublic String name;\n\tpublic double weight;\n\tpublic int durability;\n\tpublic int damage;\n\n\tpublic Sword(String name, double weight, int durability, int damage) {\n\t\tsuper();\n\t\tthis.name \u003d name;\n\t\tthis.weight \u003d weight;\n\t\tthis.durability \u003d durability;\n\t\tthis.damage \u003d damage;\n\t}\n\n\tpublic void repair(int amount) {\n\t\tdurability +\u003d amount;\n\t\tSystem.out.println(name + \" repaired by \" + amount + \". Durability\u003d\" + durability);\n\t}\n\n\tpublic void use() {\n\t\tSystem.out.println(name + \" slashes for \" + damage + \" damage!\");\n\t\tdurability -\u003d 1;\n\t}\n}\n\nclass Staff extends Item {\n\tpublic String name;\n\tpublic double weight;\n\tpublic int durability;\n\tpublic int manaBonus;\n\n\tpublic Staff(String name, double weight, int durability, int manaBonus) {\n\t\tsuper();\n\t\tthis.name \u003d name;\n\t\tthis.weight \u003d weight;\n\t\tthis.durability \u003d durability;\n\t\tthis.manaBonus \u003d manaBonus;\n\t}\n\n\tpublic void repair(int amount) {\n\t\tdurability +\u003d amount;\n\t\tSystem.out.println(name + \" repaired by \" + amount + \". Durability\u003d\" + durability);\n\t}\n\n\tpublic void use() {\n\t\tSystem.out.println(name + \" channels magic with +\" + manaBonus + \" mana!\");\n\t\tdurability -\u003d 1;\n\t}\n}\n\n"
}```
