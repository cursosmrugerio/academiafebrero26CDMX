package com.academia.rest.fake;

import com.academia.rest.entity.Alumno;
import com.academia.rest.repository.AlumnoRepository;

import org.springframework.data.domain.Example;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import java.util.*;
import java.util.function.Function;

import org.springframework.data.repository.query.FluentQuery;

/**
 * Stub manual que simula AlumnoRepository usando un HashMap en memoria.
 *
 * Proposito educativo: demostrar como testear un servicio SIN base de datos
 * y SIN frameworks de mocking. Solo implementamos los 5 metodos que
 * AlumnoService realmente usa; los demas lanzan UnsupportedOperationException.
 *
 * Esto ilustra POR QUE existen herramientas como Mockito: escribir fakes
 * manuales para interfaces grandes es tedioso y fragil.
 */
public class FakeAlumnoRepository implements AlumnoRepository {

    // Almacen en memoria: simula la coleccion de MongoDB
    private final Map<String, Alumno> datos = new HashMap<>();

    // =====================================================================
    //  Los 5 metodos que usa AlumnoService
    // =====================================================================

    @Override
    public List<Alumno> findAll() {
        return new ArrayList<>(datos.values());
    }

    @Override
    public Optional<Alumno> findById(String id) {
        return Optional.ofNullable(datos.get(id));
    }

    @Override
    @SuppressWarnings("unchecked")
    public <S extends Alumno> S save(S alumno) {
        // Si no tiene ID, generamos uno (simula el auto-generado de MongoDB)
        if (alumno.getId() == null) {
            alumno.setId(UUID.randomUUID().toString());
        }
        datos.put(alumno.getId(), alumno);
        return alumno;
    }

    @Override
    public boolean existsById(String id) {
        return datos.containsKey(id);
    }

    @Override
    public void deleteById(String id) {
        datos.remove(id);
    }

    // =====================================================================
    //  Metodos heredados NO utilizados por AlumnoService
    //  Lanzan UnsupportedOperationException para documentar que no se usan
    // =====================================================================

    @Override
    public <S extends Alumno> List<S> saveAll(Iterable<S> entities) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public List<Alumno> findAllById(Iterable<String> ids) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public long count() {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public void delete(Alumno entity) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public void deleteAllById(Iterable<? extends String> ids) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public void deleteAll(Iterable<? extends Alumno> entities) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public void deleteAll() {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public List<Alumno> findAll(Sort sort) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public Page<Alumno> findAll(Pageable pageable) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> S insert(S entity) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> List<S> insert(Iterable<S> entities) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> Optional<S> findOne(Example<S> example) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> List<S> findAll(Example<S> example) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> List<S> findAll(Example<S> example, Sort sort) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> Page<S> findAll(Example<S> example, Pageable pageable) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> long count(Example<S> example) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno> boolean exists(Example<S> example) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }

    @Override
    public <S extends Alumno, R> R findBy(Example<S> example,
            Function<FluentQuery.FetchableFluentQuery<S>, R> queryFunction) {
        throw new UnsupportedOperationException("No implementado en el fake");
    }
}
