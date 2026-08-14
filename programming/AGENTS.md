# Code Quality Guidelines

Follow these software engineering best practices:

## KISS (Keep It Simple, Stupid)
- Prefer simple, readable solutions over clever ones
- Avoid unnecessary complexity and over-engineering
- Write code that is easy to understand at first glance

## DRY (Don't Repeat Yourself)
- Extract repeated logic into reusable functions
- Use constants for repeated values
- Avoid copy-paste coding

## SOLID Principles
- **Single Responsibility**: Each function/class should do one thing well
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable for their base types
- **Interface Segregation**: Prefer small, focused interfaces
- **Dependency Inversion**: Depend on abstractions, not concretions

## General Guidelines
- Write descriptive variable and function names
- Keep functions small and focused (ideally < 20 lines)
- Add type hints to all function signatures
- Handle errors explicitly, don't silently swallow exceptions
- Prefer early returns over deep nesting
- Write code that is testable
