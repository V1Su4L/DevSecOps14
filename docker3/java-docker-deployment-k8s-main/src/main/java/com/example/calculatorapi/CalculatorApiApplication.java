package com.example.calculatorapi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class CalculatorApiApplication {

	public static void main(String[] args) {
		SpringApplication.run(CalculatorApiApplication.class, args);
	}

	private static final long MAX_AGE_SECS = 3600 * 24L;

    @Bean
    public WebMvcConfigurer corConfigurer() {
        return new WebMvcConfigurer(){
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/**")
                        .allowedOrigins("*")

                        .allowedMethods("HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE")
                        .maxAge(MAX_AGE_SECS)
                        .allowCredentials(true);
            }

        };

    }

}
