# Python Type Checking Approaches Comparison

| Feature | `typing` | `dataclasses` | `pydantic` |
|---------|----------|---------------|------------|
| **Package Type** | Built-in (Python 3.5+) | Built-in (Python 3.7+) | Third-party |
| **Installation** | No installation needed | No installation needed | `pip install pydantic` |
| **Primary Purpose** | Type hints and annotations | Auto-generate class boilerplate | Data validation and serialization |
| **Runtime Validation** | ❌ No | ❌ No | ✅ Yes |
| **Auto-generated Methods** | ❌ No | ✅ Yes (`__init__`, `__repr__`, `__eq__`, etc.) | ✅ Yes (plus validation methods) |
| **JSON Serialization** | ❌ Manual | ❌ Manual (or use `asdict()`) | ✅ Built-in (`model_dump()`, `model_dump_json()`) |
| **JSON Deserialization** | ❌ Manual | ❌ Manual | ✅ Built-in (`model_validate()`) |
| **Type Coercion** | ❌ No | ❌ No | ✅ Yes (automatic type conversion) |
| **Validation Rules** | ❌ No | ❌ No | ✅ Yes (Field validators, custom validators) |
| **Error Messages** | ❌ No runtime errors | ❌ No validation errors | ✅ Detailed validation errors |
| **Performance** | ⚡ Fast (no overhead) | ⚡ Fast | 🐌 Slightly slower (due to validation, but optimized in v2) |
| **Memory Usage** | 💚 Low | 💚 Low | 💛 Moderate (extra overhead for validation and coercion) |
| **Schema Generation** | ❌ No | ❌ No | ✅ Yes (JSON Schema, OpenAPI) |
| **IDE Support** | ✅ Excellent | ✅ Excellent | ✅ Excellent |
| **Static Type Checking** | ✅ Yes (with mypy, etc.) | ✅ Yes | ✅ Yes |
| **Immutability** | 🔧 Manual | 🔧 Optional (`frozen=True`) | 🔧 Optional |
| **Default Values** | 🔧 Manual | ✅ Easy | ✅ Easy |
| **Learning Curve** | 💚 Easy | 💚 Easy | 💛 Moderate |

## When to Use Each

### Use `typing` when:
- You only need type hints for static analysis
- Working with existing codebases
- Want minimal overhead
- Don't need runtime validation

### Use `dataclasses` when:
- Want to reduce boilerplate code
- Need basic data containers
- Want built-in Python solution
- Don't need runtime validation
- Performance is critical

### Use `pydantic` when:
- Need runtime data validation
- Working with APIs (JSON serialization/deserialization)
- Want detailed error messages
- Building web applications
- Data comes from external sources
- Need schema generation

## Code Examples

```python
# typing - Manual everything
class TypingUser:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"TypingUser(name='{self.name}', age={self.age})"

# dataclasses - Auto-generated boilerplate
from dataclasses import dataclass

@dataclass
class DataclassUser:
    name: str
    age: int

# pydantic - Validation + serialization
from pydantic import BaseModel, Field

class PydanticUser(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)
```