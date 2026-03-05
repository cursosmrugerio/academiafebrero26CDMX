package com.techshop.servicio;

import com.techshop.modelo.Categoria;
import com.techshop.repositorio.CategoriaRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class CategoriaService {

    private final CategoriaRepository categoriaRepository;

    public CategoriaService(CategoriaRepository categoriaRepository) {
        this.categoriaRepository = categoriaRepository;
    }

    public List<Categoria> listarTodas() {
        return categoriaRepository.findAll();
    }

    public Optional<Categoria> buscarPorId(String id) {
        return categoriaRepository.findById(id);
    }

    public Categoria crear(Categoria categoria) {
        if (categoriaRepository.findByNombre(categoria.getNombre()).isPresent()) {
            throw new IllegalArgumentException("Ya existe una categoria con el nombre: " + categoria.getNombre());
        }
        return categoriaRepository.save(categoria);
    }

    public Categoria actualizar(String id, Categoria categoria) {
        Categoria existente = categoriaRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Categoria no encontrada con id: " + id));
        existente.setNombre(categoria.getNombre());
        existente.setDescripcion(categoria.getDescripcion());
        existente.setAtributos(categoria.getAtributos());
        return categoriaRepository.save(existente);
    }

    public void eliminar(String id) {
        if (!categoriaRepository.existsById(id)) {
            throw new IllegalArgumentException("Categoria no encontrada con id: " + id);
        }
        categoriaRepository.deleteById(id);
    }
}
