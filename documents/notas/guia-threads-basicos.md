# Threads (Hilos) - Fundamentos en Java

## Que es un hilo?

Un hilo es una unidad de ejecucion dentro de un programa. Todo programa Java tiene al menos un hilo: el hilo `main`. Cuando creas hilos adicionales, tu programa puede hacer **varias cosas al mismo tiempo**.

**Analogia:** Un restaurante con un solo mesero atiende una mesa a la vez. Con varios meseros (hilos), se atienden varias mesas simultaneamente.

```
Sin hilos (secuencial):          Con hilos (concurrente):
┌─────────────────────┐          ┌──────────┐
│ Tarea A ── Tarea B  │          │ Tarea A  │ ──────>
│ ==================> │          │ Tarea B  │ ──────>
│ (tiempo total: A+B) │          │ (tiempo: max(A,B))
└─────────────────────┘          └──────────┘
```

### Proceso vs Hilo

| Concepto | Descripcion |
|----------|-------------|
| **Proceso** | Un programa en ejecucion (ej: Eclipse, Chrome). Tiene su propia memoria |
| **Hilo** | Una tarea dentro de un proceso. Comparte memoria con los demas hilos del mismo proceso |

---

## v0 - Crear hilos con `extends Thread`

La forma mas directa de crear un hilo: extender la clase `Thread` y sobreescribir el metodo `run()`.

### `MiHilo.java`

```java
public class MiHilo extends Thread {

    private int contador;

    public MiHilo(String nombre, int contador) {
        super(nombre); // asigna nombre al hilo
        this.contador = contador;
    }

    @Override
    public void run() {
        // Este metodo se ejecuta en un hilo separado cuando llamamos start()
        for (int i = 1; i <= contador; i++) {
            System.out.println(getName() + " -> " + i);
        }
        System.out.println(getName() + " termino!");
    }
}
```

### `Principal.java`

```java
public class Principal {

    public static void main(String[] args) {

        System.out.println("Hilo principal: " + Thread.currentThread().getName());

        MiHilo hilo1 = new MiHilo("Hilo-A", 5);
        MiHilo hilo2 = new MiHilo("Hilo-B", 5);

        // start() lanza un nuevo hilo de ejecucion
        hilo1.start();
        hilo2.start();

        System.out.println("Main continua ejecutandose...");
    }
}
```

### Posible salida (cambia cada ejecucion)

```
Hilo principal: main
Main continua ejecutandose...
Hilo-B -> 1
Hilo-A -> 1
Hilo-B -> 2
Hilo-A -> 2
Hilo-A -> 3
Hilo-B -> 3
...
```

### Puntos clave

- **`start()`** crea un hilo nuevo y ejecuta `run()` en ese hilo.
- **`run()`** llamado directamente **NO** crea un hilo nuevo — se ejecuta en el hilo actual. Este es el error mas comun de principiantes.
- El orden de ejecucion **no es determinista**: cambia cada vez que ejecutas.
- **Desventaja**: como Java no tiene herencia multiple, si ya extiendes `Thread`, no puedes extender otra clase.

---

## v1 - Crear hilos con `implements Runnable`

La forma **preferida**. Separar la tarea (`Runnable`) del mecanismo de ejecucion (`Thread`). Esto es composicion sobre herencia.

### `MiTarea.java`

```java
public class MiTarea implements Runnable {

    private String nombre;
    private int contador;

    public MiTarea(String nombre, int contador) {
        this.nombre = nombre;
        this.contador = contador;
    }

    @Override
    public void run() {
        for (int i = 1; i <= contador; i++) {
            System.out.println(nombre + " -> " + i);
        }
        System.out.println(nombre + " termino!");
    }
}
```

### `Principal.java`

```java
public class Principal {

    public static void main(String[] args) {

        // Creamos la tarea (Runnable)
        MiTarea tarea1 = new MiTarea("Tarea-A", 5);
        MiTarea tarea2 = new MiTarea("Tarea-B", 5);

        // Creamos los hilos y les pasamos la tarea
        Thread hilo1 = new Thread(tarea1);
        Thread hilo2 = new Thread(tarea2);

        hilo1.start();
        hilo2.start();

        System.out.println("Main continua...");
    }
}
```

### Por que es mejor que `extends Thread`?

| `extends Thread` | `implements Runnable` |
|---|---|
| La clase **es** un hilo | La clase **tiene** una tarea |
| No puedes extender otra clase | Puedes extender cualquier clase |
| Mezcla la tarea con el mecanismo | Separa responsabilidades |
| Menos flexible | Mas flexible y reutilizable |

> **Regla:** Usa `Runnable` a menos que necesites sobreescribir otros metodos de `Thread` (raro).

---

## v2 - Hilos con expresiones lambda

`Runnable` es una **interfaz funcional** (tiene un solo metodo abstracto: `run()`). Eso significa que podemos usar lambdas en vez de crear una clase aparte.

### `Principal.java`

```java
public class Principal {

    public static void main(String[] args) {

        // Lambda: forma compacta de implementar Runnable
        Thread hilo1 = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Lambda-A -> " + i);
            }
        });

        Thread hilo2 = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Lambda-B -> " + i);
            }
        });

        hilo1.start();
        hilo2.start();

        // Forma ultra compacta para tareas simples
        new Thread(() -> System.out.println("Hilo de una sola linea!")).start();

        System.out.println("Main continua...");
    }
}
```

### Evolucion: de v0 a v2

```java
// v0: extends Thread (clase completa)
class MiHilo extends Thread {
    public void run() { System.out.println("Hola"); }
}
new MiHilo().start();

// v1: implements Runnable (clase separada)
class MiTarea implements Runnable {
    public void run() { System.out.println("Hola"); }
}
new Thread(new MiTarea()).start();

// v1.5: clase anonima
new Thread(new Runnable() {
    public void run() { System.out.println("Hola"); }
}).start();

// v2: lambda
new Thread(() -> System.out.println("Hola")).start();
```

Las cuatro hacen lo mismo. Lambda es la forma moderna y compacta.

---

## v3 - `sleep()`: simular tareas que toman tiempo

`Thread.sleep(milisegundos)` pausa el hilo actual. Mientras un hilo duerme, otros hilos pueden ejecutarse.

### `Principal.java`

```java
public class Principal {

    public static void main(String[] args) {

        Thread descarga1 = new Thread(() -> descargarArchivo("foto.jpg", 3));
        Thread descarga2 = new Thread(() -> descargarArchivo("video.mp4", 5));
        Thread descarga3 = new Thread(() -> descargarArchivo("musica.mp3", 2));

        descarga1.start();
        descarga2.start();
        descarga3.start();

        System.out.println("Descargas iniciadas... el main no se bloquea!");
    }

    static void descargarArchivo(String nombre, int segundos) {
        System.out.println("Iniciando descarga de " + nombre + "...");

        for (int i = 1; i <= segundos; i++) {
            try {
                Thread.sleep(1000); // pausa 1 segundo
            } catch (InterruptedException e) {
                System.out.println("Descarga de " + nombre + " fue interrumpida!");
                return;
            }
            System.out.println(nombre + " -> " + i + "/" + segundos + " segundos");
        }

        System.out.println(nombre + " descargado!");
    }
}
```

### Posible salida

```
Descargas iniciadas... el main no se bloquea!
Iniciando descarga de foto.jpg...
Iniciando descarga de video.mp4...
Iniciando descarga de musica.mp3...
musica.mp3 -> 1/2 segundos
foto.jpg -> 1/3 segundos
video.mp4 -> 1/5 segundos
musica.mp3 -> 2/2 segundos
musica.mp3 descargado!              <-- termina primero (2 seg)
foto.jpg -> 2/3 segundos
video.mp4 -> 2/5 segundos
foto.jpg -> 3/3 segundos
foto.jpg descargado!                <-- termina segundo (3 seg)
video.mp4 -> 3/5 segundos
video.mp4 -> 4/5 segundos
video.mp4 -> 5/5 segundos
video.mp4 descargado!              <-- termina ultimo (5 seg)
```

### Puntos clave

- `sleep()` **siempre** requiere manejar `InterruptedException` (checked exception).
- `sleep()` pausa el hilo **actual**, no otro hilo.
- Mientras un hilo duerme, el procesador atiende otros hilos.
- Las tres descargas corren **en paralelo**: el tiempo total es ~5 seg, no 3+5+2=10 seg.

---

## v4 - `join()`: esperar a que terminen los hilos

Sin `join()`, el hilo `main` puede terminar antes que los hilos hijos. Con `join()`, le dices a `main`: "espera aqui hasta que este hilo termine".

### `Principal.java`

```java
public class Principal {

    public static void main(String[] args) {

        Thread hilo1 = new Thread(() -> {
            System.out.println("Hilo-1: Consultando base de datos...");
            pausar(3000);
            System.out.println("Hilo-1: Consulta terminada!");
        });

        Thread hilo2 = new Thread(() -> {
            System.out.println("Hilo-2: Llamando API externa...");
            pausar(2000);
            System.out.println("Hilo-2: Respuesta recibida!");
        });

        Thread hilo3 = new Thread(() -> {
            System.out.println("Hilo-3: Procesando archivo...");
            pausar(1000);
            System.out.println("Hilo-3: Archivo procesado!");
        });

        long inicio = System.currentTimeMillis();

        hilo1.start();
        hilo2.start();
        hilo3.start();

        // join() hace que main ESPERE a que cada hilo termine
        try {
            hilo1.join();
            hilo2.join();
            hilo3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        long duracion = System.currentTimeMillis() - inicio;

        System.out.println("Todas las tareas terminaron en " + duracion + " ms");
        System.out.println("(Sin hilos habrian tardado ~6000 ms)");
    }

    static void pausar(int milisegundos) {
        try {
            Thread.sleep(milisegundos);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

### Salida

```
Hilo-1: Consultando base de datos...
Hilo-2: Llamando API externa...
Hilo-3: Procesando archivo...
Hilo-3: Archivo procesado!          <-- 1 seg
Hilo-2: Respuesta recibida!         <-- 2 seg
Hilo-1: Consulta terminada!         <-- 3 seg
Todas las tareas terminaron en 3005 ms
(Sin hilos habrian tardado ~6000 ms)
```

### Diagrama de tiempo

```
Sin hilos (secuencial):
main: [===BD 3s===][==API 2s==][=Archivo 1s=]  Total: 6 seg

Con hilos (concurrente):
hilo1: [===BD 3s===]
hilo2: [==API 2s==]                              Total: 3 seg
hilo3: [=Arch 1s=]                               (el maximo)
main:  ............join().........|continua-->
```

### Punto clave

`join()` es esencial cuando necesitas los **resultados** de los hilos antes de continuar. Ejemplo real: lanzar 3 consultas en paralelo y combinar los resultados cuando todas terminen.

---

## v5 - Race Condition: el peligro de los recursos compartidos

Cuando dos hilos leen y escriben la **misma variable** al mismo tiempo, el resultado es impredecible. Esto se llama **race condition** (condicion de carrera).

### `Contador.java`

```java
public class Contador {

    private int valor = 0;

    // Este metodo NO es thread-safe
    // Internamente, valor++ son 3 operaciones: leer, sumar, escribir
    // Si dos hilos lo ejecutan al mismo tiempo, pueden pisar los valores del otro
    public void incrementar() {
        valor++;
    }

    public int getValor() {
        return valor;
    }
}
```

### `Principal.java`

```java
public class Principal {

    public static void main(String[] args) throws InterruptedException {

        Contador contador = new Contador(); // recurso COMPARTIDO

        Thread hilo1 = new Thread(() -> {
            for (int i = 0; i < 10_000; i++) {
                contador.incrementar();
            }
        });

        Thread hilo2 = new Thread(() -> {
            for (int i = 0; i < 10_000; i++) {
                contador.incrementar();
            }
        });

        hilo1.start();
        hilo2.start();

        hilo1.join();
        hilo2.join();

        System.out.println("Resultado esperado: 20000");
        System.out.println("Resultado real:     " + contador.getValor());
    }
}
```

### Salida (diferente cada vez)

```
Resultado esperado: 20000
Resultado real:     13289
HAY UN PROBLEMA! Los hilos se pisaron entre si.
Esto se llama RACE CONDITION.
```

### Por que pasa esto?

`valor++` parece una operacion, pero internamente son **tres pasos**:

```
1. LEER:    temp = valor     (leer el valor actual)
2. SUMAR:   temp = temp + 1  (sumarle 1)
3. ESCRIBIR: valor = temp    (guardar el nuevo valor)
```

Si dos hilos ejecutan esto al mismo tiempo:

```
valor = 5

Hilo-A: LEE valor (5)
                          Hilo-B: LEE valor (5)     <-- lee el MISMO 5
Hilo-A: SUMA (5+1=6)
                          Hilo-B: SUMA (5+1=6)
Hilo-A: ESCRIBE valor=6
                          Hilo-B: ESCRIBE valor=6   <-- pisa el 6 de A

Resultado: valor=6 (deberia ser 7, se "perdio" un incremento)
```

### Solucion (tema de la siguiente clase)

```java
// Agregar synchronized al metodo para que solo un hilo a la vez lo ejecute
public synchronized void incrementar() {
    valor++;
}
```

---

## Resumen de metodos

| Metodo | Que hace | Ejemplo |
|--------|----------|---------|
| `start()` | Crea un hilo nuevo y ejecuta `run()` en el | `hilo.start()` |
| `run()` | Contiene el codigo que ejecuta el hilo | Sobreescribir en tu clase |
| `sleep(ms)` | Pausa el hilo actual N milisegundos | `Thread.sleep(1000)` |
| `join()` | Espera a que el hilo termine | `hilo.join()` |
| `getName()` | Obtiene el nombre del hilo | `hilo.getName()` |
| `currentThread()` | Referencia al hilo que esta ejecutando | `Thread.currentThread()` |

## Resumen de las tres formas de crear hilos

| Forma | Cuando usarla |
|-------|---------------|
| `extends Thread` | Casi nunca. Solo si necesitas sobreescribir metodos de Thread |
| `implements Runnable` | Cuando necesitas una clase con estado o reutilizable |
| Lambda | Para tareas cortas y simples (la mas comun en codigo moderno) |

## Que viene despues?

- **`synchronized`** — proteger recursos compartidos
- **`wait()` / `notify()`** — comunicacion entre hilos
- **`ExecutorService`** — pool de hilos (manejo moderno)
- **`Future` / `CompletableFuture`** — obtener resultados de hilos

## Referencias

- [Java Threads - Oracle Tutorial](https://docs.oracle.com/javase/tutorial/essential/concurrency/)
- [Baeldung - Java Concurrency](https://www.baeldung.com/java-concurrency)
- [Java Thread vs Runnable](https://www.baeldung.com/java-runnable-vs-extending-thread)
