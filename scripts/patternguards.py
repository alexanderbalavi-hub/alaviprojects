from uebung.geometricshapes import Circle,Square,Rectangle
# create a list of some shapes

def main():
    shapes = [Circle(5), Square(4), Rectangle(4,5), Square(7), Circle(9), Rectangle(3,10)]    

    # use pattern matching to process each shape
    # include pattern guards for mnore detailed processing

    for shape in shapes:
        match shape:
            case Circle():
                print(f"Circle with area {shape.getArea()}")
            case Square():
                print(f"Square with area {shape.getArea()}")
            case Rectangle():
                print(f"Rectangle with area {shape.getArea()}")
            case _:
                print(f"Unrecognized shape: {type(shape)}")     

if __name__ == "__main__":
    main()
