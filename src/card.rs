use pyo3::prelude::*;

#[pyclass]
pub struct Card {
    key: string, 
    value: string,
}

#[pymethods]
impl Card {
    #[new]
    fn new(key: string, value: string) -> Self {
        Card(key, value);
    }

    fn get_key(&self) -> string {
        self.key
    }

    fn get_value(&self) -> string {
        self.value
    }
}