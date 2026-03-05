package com.techshop.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI techShopOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("TechShop Ecommerce API")
                        .description("API REST para tienda de electronica - Proyecto final academia BBVA")
                        .version("1.0.0")
                        .contact(new Contact()
                                .name("Miguel Rugerio")
                                .email("miguel.rugerio@outlook.com")));
    }
}
