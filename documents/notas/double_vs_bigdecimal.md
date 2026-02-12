# `double` vs `BigDecimal` en Java

## El problema central

`double` usa representacion binaria de punto flotante (IEEE 754). Esto significa que **no puede representar ciertos numeros decimales de forma exacta**. Ejemplo clasico:

```java
System.out.println(0.1 + 0.2);
// Esperarias: 0.3
// Obtienes:   0.30000000000000004
```

Esto NO es un bug de Java. Es una limitacion fundamental de como las computadoras almacenan decimales en binario.

## `double` - Rapido pero impreciso

```java
double a = 0.1;
double b = 0.2;
double resultado = a + b;
// resultado = 0.30000000000000004  <- error de precision
```

- Ocupa **8 bytes** en memoria
- Operaciones son **muy rapidas** (el procesador las hace directamente)
- Tiene ~15-17 digitos de precision
- Los errores se **acumulan** con cada operacion

## `BigDecimal` - Lento pero exacto

```java
BigDecimal a = new BigDecimal("0.1");
BigDecimal b = new BigDecimal("0.2");
BigDecimal resultado = a.add(b);
// resultado = 0.3  <- exacto
```

- Ocupa **mas memoria** (es un objeto, no un tipo primitivo)
- Operaciones son **mas lentas** (~100x mas lento que `double`)
- Precision **arbitraria** (tantos decimales como necesites)
- No acumula errores de redondeo

## Cuidado con este error comun

```java
// MAL - esto sigue teniendo el problema del double
BigDecimal malo = new BigDecimal(0.1);
System.out.println(malo);
// 0.1000000000000000055511151231257827021181583404541015625

// BIEN - usar String evita el problema
BigDecimal bueno = new BigDecimal("0.1");
System.out.println(bueno);
// 0.1
```

Siempre usa el constructor con **String** o `BigDecimal.valueOf()`.

## Cuando usar cada uno

| Situacion | Usa |
|---|---|
| **Dinero, finanzas, facturacion** | `BigDecimal` |
| **Calculos cientificos donde la precision importa** | `BigDecimal` |
| **Graficos, juegos, animaciones** | `double` |
| **Calculos donde un pequeno error es aceptable** | `double` |
| **Rendimiento critico (millones de operaciones)** | `double` |

## La regla de oro

> Si el numero representa **dinero** o algo donde los centavos importan, usa `BigDecimal`. Para todo lo demas, `double` probablemente esta bien.

Imagina un sistema bancario que procesa millones de transacciones. Un error de `0.000000004` por operacion se acumula y terminas con miles de pesos de diferencia. Por eso los sistemas financieros **siempre** usan `BigDecimal`.

## Ejemplo practico

```java
// Simulando una tienda con double (PELIGROSO)
double precioDouble = 19.99;
double totalDouble = precioDouble * 1000;
System.out.println(totalDouble); // Podria dar 19989.999999999996

// Simulando una tienda con BigDecimal (SEGURO)
BigDecimal precioBD = new BigDecimal("19.99");
BigDecimal totalBD = precioBD.multiply(new BigDecimal("1000"));
System.out.println(totalBD); // 19990.00 exacto
```

## Resumen

`double` es el carro deportivo (rapido pero impreciso), `BigDecimal` es el contador (lento pero no pierde ni un centavo).

## Referencias

- [Java Double vs. BigDecimal | Baeldung](https://www.baeldung.com/java-double-vs-bigdecimal)
- [Java Double vs. BigDecimal - Java Code Geeks](https://examples.javacodegeeks.com/java-double-vs-bigdecimal/)
- [StackOverflow: Double vs BigDecimal](https://stackoverflow.com/questions/3413448/double-vs-bigdecimal)
