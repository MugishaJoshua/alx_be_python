from class_static_methods_demo import Calculator

def main():
    sum_result = Calculator.add(10, 5)
    product_result = Calculator.multiply(10, 5)

    print(f"The sum is: {sum_result}")
    print(f"Calculation type: {Calculator.calculation_type}")
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
