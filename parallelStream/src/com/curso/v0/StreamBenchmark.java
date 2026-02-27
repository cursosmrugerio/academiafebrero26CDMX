package com.curso.v0;

import java.util.*;
import java.util.stream.*;
import java.util.concurrent.atomic.AtomicLong;
import java.util.function.Supplier;

/**
 * ============================================================
 *  BENCHMARK: Stream vs Parallel Stream en Java
 * ============================================================
 *  Este programa compara el rendimiento de operaciones
 *  secuenciales (stream) vs paralelas (parallelStream)
 *  en diferentes escenarios reales.
 * 
 *  @author Miguel
 * ============================================================
 */
public class StreamBenchmark {

    // ─── Constantes de configuración ───
    private static final int SMALL_SIZE    = 1_000;
    private static final int MEDIUM_SIZE   = 100_000;
    private static final int LARGE_SIZE    = 10_000_000;
    private static final int WARMUP_ROUNDS = 3;
    private static final int TEST_ROUNDS   = 5;
    //double d = 1000.00;

    // ─── Colores ANSI para consola ───
    static final String RESET  = "\u001B[0m";
    static final String GREEN  = "\u001B[32m";
    static final String YELLOW = "\u001B[33m";
    static final String CYAN   = "\u001B[36m";
    static final String RED    = "\u001B[31m";
    static final String BOLD   = "\u001B[1m";
    static final String DIM    = "\u001B[2m";

    public static void main(String[] args) {
        printHeader();
        printSystemInfo();

        // Generar datos de prueba
        System.out.println(CYAN + "\n⏳ Generando datos de prueba..." + RESET);
        List<Integer> smallList  = generateRandomList(SMALL_SIZE);
        List<Integer> mediumList = generateRandomList(MEDIUM_SIZE);
        List<Integer> largeList  = generateRandomList(LARGE_SIZE);
        List<String>  stringList = generateStringList(LARGE_SIZE);
        System.out.println(GREEN + "✓ Datos generados correctamente\n" + RESET);

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 1: Operación ligera (sum) - diferentes tamaños
        // ══════════════════════════════════════════════════════
        printScenarioHeader("1", "OPERACIÓN LIGERA (suma de enteros)",
                "Compara cómo el tamaño de la colección afecta la ventaja del paralelismo");

        benchmark("Suma - 1K elementos", 
            () -> smallList.stream().mapToLong(Integer::longValue).sum(),
            () -> smallList.parallelStream().mapToLong(Integer::longValue).sum()
        );

        benchmark("Suma - 100K elementos",
            () -> mediumList.stream().mapToLong(Integer::longValue).sum(),
            () -> mediumList.parallelStream().mapToLong(Integer::longValue).sum()
        );

        benchmark("Suma - 10M elementos",
            () -> largeList.stream().mapToLong(Integer::longValue).sum(),
            () -> largeList.parallelStream().mapToLong(Integer::longValue).sum()
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 2: Operación pesada (cálculo CPU-intensivo)
        // ══════════════════════════════════════════════════════
        printScenarioHeader("2", "OPERACIÓN PESADA (cálculos matemáticos intensivos)",
                "Aquí el paralelismo brilla porque cada elemento requiere mucho procesamiento");

        benchmark("Cálculo pesado - 100K elementos",
            () -> mediumList.stream()
                    .mapToDouble(n -> heavyComputation(n))
                    .sum(),
            () -> mediumList.parallelStream()
                    .mapToDouble(n -> heavyComputation(n))
                    .sum()
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 3: Filtrado + Transformación + Recolección
        // ══════════════════════════════════════════════════════
        printScenarioHeader("3", "PIPELINE COMPLEJO (filter → map → collect)",
                "Pipeline típico: filtrar pares, transformar y recolectar en lista");

        benchmark("Pipeline complejo - 10M elementos",
            () -> largeList.stream()
                    .filter(n -> n % 2 == 0)
                    .map(n -> n * n)
                    .filter(n -> n > 1000)
                    .mapToLong(Integer::longValue)
                    .sum(),
            () -> largeList.parallelStream()
                    .filter(n -> n % 2 == 0)
                    .map(n -> n * n)
                    .filter(n -> n > 1000)
                    .mapToLong(Integer::longValue)
                    .sum()
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 4: Operaciones con Strings
        // ══════════════════════════════════════════════════════
        printScenarioHeader("4", "PROCESAMIENTO DE STRINGS",
                "Operaciones con cadenas: uppercase, filtrado por longitud, distinct");

        benchmark("Strings - 10M elementos",
            () -> stringList.stream()
                    .map(String::toUpperCase)
                    .filter(s -> s.length() > 5)
                    .distinct()
                    .count(),
            () -> stringList.parallelStream()
                    .map(String::toUpperCase)
                    .filter(s -> s.length() > 5)
                    .distinct()
                    .count()
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 5: Reducción personalizada
        // ══════════════════════════════════════════════════════
        printScenarioHeader("5", "REDUCCIÓN PERSONALIZADA (encontrar máximo con reduce)",
                "Usa reduce() para encontrar el valor máximo - operación asociativa");

        benchmark("Reduce max - 10M elementos",
            () -> largeList.stream()
                    .reduce(Integer.MIN_VALUE, Integer::max),
            () -> largeList.parallelStream()
                    .reduce(Integer.MIN_VALUE, Integer::max)
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 6: Agrupamiento (groupingBy)
        // ══════════════════════════════════════════════════════
        printScenarioHeader("6", "AGRUPAMIENTO (groupingBy)",
                "Agrupar elementos por residuo mod 100 - requiere merge de resultados parciales");

        benchmark("GroupingBy - 10M elementos",
            () -> largeList.stream()
                    .collect(Collectors.groupingBy(n -> n % 100, Collectors.counting())),
            () -> largeList.parallelStream()
                    .collect(Collectors.groupingByConcurrent(n -> n % 100, Collectors.counting()))
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 7: Sorted (operación con estado)
        // ══════════════════════════════════════════════════════
        printScenarioHeader("7", "ORDENAMIENTO (sorted) - Stateful operation",
                "sorted() es una operación con estado que puede ser costosa en paralelo");

        List<Integer> sortTestList = generateRandomList(1_000_000);
        benchmark("Sorted - 1M elementos",
            () -> sortTestList.stream()
                    .sorted()
                    .limit(100)
                    .collect(Collectors.toList()),
            () -> sortTestList.parallelStream()
                    .sorted()
                    .limit(100)
                    .collect(Collectors.toList())
        );

        // ══════════════════════════════════════════════════════
        //  ESCENARIO 8: Operación con efecto secundario (mal uso)
        // ══════════════════════════════════════════════════════
        printScenarioHeader("8", "⚠️  ANTIPATRÓN: forEach con estado compartido",
                "Demuestra por qué NO se debe usar parallelStream con estado mutable compartido");

        demonstrateSideEffectProblem(mediumList);

        // ══════════════════════════════════════════════════════
        //  RESUMEN FINAL
        // ══════════════════════════════════════════════════════
        printConclusions();
    }

    // ═══════════════════════════════════════════════════════════
    //  MÉTODOS DE BENCHMARK
    // ═══════════════════════════════════════════════════════════

    @SuppressWarnings("unchecked")
    static <T> void benchmark(String testName, Supplier<T> sequential, Supplier<T> parallel) {
        System.out.printf("  %s%-40s%s", BOLD, testName, RESET);
        System.out.println();

        // Warmup (el JIT necesita calentar motores)
        for (int i = 0; i < WARMUP_ROUNDS; i++) {
            sequential.get();
            parallel.get();
        }

        // Test secuencial
        long[] seqTimes = new long[TEST_ROUNDS];
        for (int i = 0; i < TEST_ROUNDS; i++) {
            long start = System.nanoTime();
            sequential.get();
            seqTimes[i] = System.nanoTime() - start;
        }

        // Test paralelo
        long[] parTimes = new long[TEST_ROUNDS];
        for (int i = 0; i < TEST_ROUNDS; i++) {
            long start = System.nanoTime();
            parallel.get();
            parTimes[i] = System.nanoTime() - start;
        }

        // Calcular promedios (descartando outliers: min y max)
        double seqAvg = trimmedAverage(seqTimes);
        double parAvg = trimmedAverage(parTimes);
        double speedup = seqAvg / parAvg;

        // Mostrar resultados
        String seqFormatted = formatNanos(seqAvg);
        String parFormatted = formatNanos(parAvg);

        System.out.printf("    %s🔵 Stream (secuencial):%s  %s%n", DIM, RESET, seqFormatted);
        System.out.printf("    %s🟢 Parallel Stream:    %s  %s%n", DIM, RESET, parFormatted);

        if (speedup > 1.1) {
            System.out.printf("    %s⚡ Speedup: %.2fx más rápido con parallel%s%n", GREEN, speedup, RESET);
        } else if (speedup < 0.9) {
            System.out.printf("    %s🐢 Slowdown: %.2fx más lento con parallel%s%n", RED, 1.0 / speedup, RESET);
        } else {
            System.out.printf("    %s≈  Rendimiento similar (%.2fx)%s%n", YELLOW, speedup, RESET);
        }

        // Barra visual de comparación
        printComparisonBar(seqAvg, parAvg);
        System.out.println();
    }

    // ═══════════════════════════════════════════════════════════
    //  DEMOSTRACIÓN DE ANTIPATRÓN
    // ═══════════════════════════════════════════════════════════

    static void demonstrateSideEffectProblem(List<Integer> list) {
        System.out.println(YELLOW + "  Intentando sumar con ArrayList (NO thread-safe):" + RESET);

        // Secuencial - siempre correcto
        List<Integer> seqResult = new ArrayList<>();
        list.stream().filter(n -> n % 2 == 0).forEach(seqResult::add);
        int expectedSize = seqResult.size();

        // Parallel - resultado impredecible con ArrayList
        int errores = 0;
        int intentos = 10;
        for (int i = 0; i < intentos; i++) {
            try {
                List<Integer> parResult = new ArrayList<>();
                list.parallelStream().filter(n -> n % 2 == 0).forEach(parResult::add);
                if (parResult.size() != expectedSize) {
                    errores++;
                }
            } catch (Exception e) {
                errores++;
            }
        }

        System.out.printf("    %s→ Resultado secuencial: %d elementos (siempre correcto)%s%n",
                GREEN, expectedSize, RESET);
        System.out.printf("    %s→ Parallel con ArrayList: %d/%d ejecuciones con errores o datos incorrectos%s%n",
                errores > 0 ? RED : GREEN, errores, intentos, RESET);

        System.out.println();
        System.out.println(CYAN + "  ✅ Forma CORRECTA con parallel:" + RESET);
        System.out.println(DIM + "    // Usar collect() en lugar de forEach() con estado mutable" + RESET);
        System.out.println(DIM + "    List<Integer> result = list.parallelStream()" + RESET);
        System.out.println(DIM + "        .filter(n -> n % 2 == 0)" + RESET);
        System.out.println(DIM + "        .collect(Collectors.toList());" + RESET);

        List<Integer> correctParallel = list.parallelStream()
                .filter(n -> n % 2 == 0)
                .collect(Collectors.toList());
        System.out.printf("    %s→ Collect paralelo: %d elementos (siempre correcto ✓)%s%n%n",
                GREEN, correctParallel.size(), RESET);
    }

    // ═══════════════════════════════════════════════════════════
    //  MÉTODOS AUXILIARES
    // ═══════════════════════════════════════════════════════════

    static double heavyComputation(int n) {
        double result = n;
        for (int i = 0; i < 50; i++) {
            result = Math.sin(result) * Math.cos(result) + Math.sqrt(Math.abs(result));
        }
        return result;
    }

    static List<Integer> generateRandomList(int size) {
        Random random = new Random(42); // Seed fija para reproducibilidad
        return random.ints(size, 0, 10_000)
                .boxed()
                .collect(Collectors.toList());
    }

    static List<String> generateStringList(int size) {
        Random random = new Random(42);
        String[] words = {"Java", "Stream", "Parallel", "Benchmark", "Performance",
                "Lambda", "Functional", "Pipeline", "Thread", "CPU",
                "Map", "Filter", "Reduce", "Collect", "Spring"};
        List<String> list = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            list.add(words[random.nextInt(words.length)] + random.nextInt(1000));
        }
        return list;
    }

    static double trimmedAverage(long[] times) {
        if (times.length <= 2) {
            return Arrays.stream(times).average().orElse(0);
        }
        Arrays.sort(times);
        long sum = 0;
        for (int i = 1; i < times.length - 1; i++) {
            sum += times[i];
        }
        return (double) sum / (times.length - 2);
    }

    static String formatNanos(double nanos) {
        if (nanos < 1_000) return String.format("%.0f ns", nanos);
        if (nanos < 1_000_000) return String.format("%.2f µs", nanos / 1_000);
        if (nanos < 1_000_000_000) return String.format("%.2f ms", nanos / 1_000_000);
        return String.format("%.2f s", nanos / 1_000_000_000);
    }

    static void printComparisonBar(double seqAvg, double parAvg) {
        int maxBarLen = 40;
        double maxVal = Math.max(seqAvg, parAvg);

        int seqBar = (int) (seqAvg / maxVal * maxBarLen);
        int parBar = (int) (parAvg / maxVal * maxBarLen);

        System.out.printf("    Seq: %s%s%s%n", YELLOW, "█".repeat(Math.max(1, seqBar)), RESET);
        System.out.printf("    Par: %s%s%s%n", GREEN, "█".repeat(Math.max(1, parBar)), RESET);
    }

    // ═══════════════════════════════════════════════════════════
    //  PRESENTACIÓN
    // ═══════════════════════════════════════════════════════════

    static void printHeader() {
        System.out.println(CYAN + BOLD);
        System.out.println("╔══════════════════════════════════════════════════════════╗");
        System.out.println("║                                                          ║");
        System.out.println("║     ⚡ Stream vs Parallel Stream - Benchmark ⚡          ║");
        System.out.println("║                                                          ║");
        System.out.println("║     Comparativa de rendimiento en Java                   ║");
        System.out.println("║                                                          ║");
        System.out.println("╚══════════════════════════════════════════════════════════╝");
        System.out.println(RESET);
    }

    static void printSystemInfo() {
        Runtime runtime = Runtime.getRuntime();
        System.out.println(DIM + "─── Información del Sistema ───" + RESET);
        System.out.printf("  Procesadores disponibles: %s%d cores%s%n", BOLD, runtime.availableProcessors(), RESET);
        System.out.printf("  JVM: %s%s%s%n", BOLD, System.getProperty("java.version"), RESET);
        System.out.printf("  Memoria máxima: %s%d MB%s%n", BOLD, runtime.maxMemory() / (1024 * 1024), RESET);
        System.out.printf("  ForkJoinPool parallelism: %s%d%s%n", BOLD,
                java.util.concurrent.ForkJoinPool.commonPool().getParallelism(), RESET);
        System.out.printf("  Warmup rounds: %d | Test rounds: %d%n", WARMUP_ROUNDS, TEST_ROUNDS);
    }

    static void printScenarioHeader(String number, String title, String description) {
        System.out.println(CYAN + "━".repeat(60) + RESET);
        System.out.printf("%s  ESCENARIO %s: %s%s%n", BOLD, number, title, RESET);
        System.out.printf("%s  %s%s%n", DIM, description, RESET);
        System.out.println(CYAN + "━".repeat(60) + RESET);
    }

    static void printConclusions() {
        System.out.println();
        System.out.println(CYAN + BOLD + "╔══════════════════════════════════════════════════════════╗" + RESET);
        System.out.println(CYAN + BOLD + "║              📝 CONCLUSIONES Y BUENAS PRÁCTICAS         ║" + RESET);
        System.out.println(CYAN + BOLD + "╚══════════════════════════════════════════════════════════╝" + RESET);
        System.out.println();
        System.out.println(GREEN  + "  ✅ USA parallelStream() cuando:" + RESET);
        System.out.println("     • La colección es GRANDE (>100K elementos)");
        System.out.println("     • Cada operación por elemento es COSTOSA (CPU-bound)");
        System.out.println("     • Las operaciones son independientes entre sí");
        System.out.println("     • Usas collect() en vez de forEach() con estado mutable");
        System.out.println("     • La fuente de datos se divide fácilmente (ArrayList, arrays)");
        System.out.println();
        System.out.println(RED    + "  ❌ EVITA parallelStream() cuando:" + RESET);
        System.out.println("     • La colección es pequeña (<10K elementos)");
        System.out.println("     • Las operaciones son simples/rápidas");
        System.out.println("     • Hay estado compartido mutable (ArrayList, HashMap)");
        System.out.println("     • La fuente es LinkedList (mal splitting)");
        System.out.println("     • Las operaciones tienen efectos secundarios");
        System.out.println("     • Hay operaciones ordenadas con sorted()/limit()");
        System.out.println();
        System.out.println(YELLOW + "  💡 RECUERDA:" + RESET);
        System.out.println("     • El overhead de crear hilos no es gratis");
        System.out.println("     • parallelStream() usa el ForkJoinPool.commonPool()");
        System.out.println("     • Siempre MIDE antes de decidir usar parallel");
        System.out.println("     • El número de cores del CPU afecta directamente el speedup");
        System.out.println();
    }
}
