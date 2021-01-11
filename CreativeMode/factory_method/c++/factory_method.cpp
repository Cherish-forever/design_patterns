#include <iostream>
#include <string>

class Product {
public:
  virtual ~Product() {}
  virtual std::string Operation() const = 0;
};

class ConcreateProduct1: public Product {
public:
  std::string Operation() const override {
    return "{Result of the ConcreateProduct1}";
  }
};

class ConcreateProduct2: public Product {
public:
  std::string Operation() const override {
    return "{Result of the ConcreateProduct2}";
  }
};

class Creator {
public:
  virtual ~Creator() {};
  virtual Product* FactoryMethod() const = 0;

  std::string SomeOperation() const {
    Product* product = this->FactoryMethod();
    std::string result = "Creator: The same creator`s code has just worked with "+
      product->Operation();
    delete product;
    return result;
  }
};

class ConcreateCreator1 : public Creator {
public:
  Product *FactoryMethod() const override {
    return new ConcreateProduct1();
  }
};

class ConcreateCreator2 : public Creator {
public:
  Product *FactoryMethod() const override {
    return new ConcreateProduct2();
  }
};

void ClientCode(const Creator& creator) {
  std::cout << "Client: I`m not aware of the creator`s class, but it still works.\n"
	     << creator.SomeOperation() << std::endl;
}

int main() {
  std::cout << "App: Launched with the ConcreateCreator1.\n";
  Creator *creator = new ConcreateCreator1();
  ClientCode(*creator);
  std::cout << std::endl;
  std::cout << "App: Launched with the ConcreateCreator2.\n";
  Creator *creator2 = new ConcreateCreator2();
  ClientCode(*creator2);
  delete creator;
  delete creator2;
  return 0;
}
