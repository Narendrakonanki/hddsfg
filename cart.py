products=['bags','pens','books','pencils','chocos']
quantity=[4,6,3,5]
price=[20,12,18,5]
user_list=[]
user_items=[]




while True:
    role=input("who are you (admin/user):")
    if role=="admin":

        admin_name=input("enter the name:").lower()
        password=int(input("enter the password:"))
        
        if admin_name=="nari" and password==123:
            

            print("1.add product")
            print("2.update product")
            print("3.remove product")
            print("4.view products")
            print("5.view users")
            print("6.exit")
        

            while True:
                choose=int(input("enter your choice:"))

                if choose==1:
                    while True:
                        item=input("enter the products/ for exit tye over:")
                        if item=="over":
                            break
                        quant=int(input("product quantity:"))
                        money=int(input("enter the amount for items:"))
                        
                        products.append(item)
                        quantity.append(quant)
                        price.append(money)

                        print(products,"\n",quantity,"\n",price,"\n")
                        

                elif choose==2:
                    while True:
                        update_product=input("enter the updated product/ over:")
                        if update_product=="over":
                                print("Updated Products:",products)
                                print("updated quantity:",quantity)
                                print("updated price:",price)
                            
                                break
                        update_quantity=int(input("enter the quantity:"))
                        update_price=int(input("enter updated price:"))
                        
                        
                        
                        index_value=int(input("enter the index value:"))
                        if index_value < len(products):
                            
                            products[index_value]=update_product
                            quantity[index_value]=update_quantity
                            price[index_value]=update_price
                            
                            
                        else:
                            print("index range is out of bound")
                        
                    
                elif choose==3:
                    while True:
                        remove_product=input("enter the product/ for exit type over:")
                        
                        if remove_product in products:
                            index_value=products.index(remove_product)
                            products.pop(index_value)
                            price.pop(index_value)
                            quantity.pop(index_value)
                            
                            print(remove_product," is removed from products list")
                        elif remove_product=="over":
                            break
                        else:
                            print(remove_product," is not in the list")
                            
                elif choose==4:
                    print(products)
                    print(quantity)
                    print(price)

                elif choose==5:
                     for i in range(len(user_list)):
                            print(user_list[i], ":", user_items[i])
                   
                            
                        
                    
                    
                    

                elif choose==6:
                    print("exit")
                    break
                else:
                    print("invalid choice")
        else:
            print("Invalid credentials")

                
    if role=="user":
            user_name=input("enter the name :")
            if user_name not in user_list:
                
                    user_list.append(user_name)
                    user_items.append([])
            user_index = user_list.index(user_name)
            amnt=0
            cart_list=[]
            cart_quantity=[]
            cart_amount=[]
            
            
            print("1.view products")
            print("2.add to cart")
            print("3.remove from cart")
            print("4.view cart")
            print("5.check out")
            print("6.exit")

            while True:
                choose=int(input("enter the  your option:"))
                  
                if choose==1:
                    print(products)
                    print(quantity)
                    print(price)

                elif choose==2:
                    while True:
                        product=input("enter a product/for exist type over:")
                        
                        if product in products:
                            qty=int(input("how much do you want:"))
                            
                            index_value=products.index(product)
                            if qty<=quantity[index_value]:
                                
                                amnt=qty*price[index_value]    
                                cart_list.append(product)
                                user_items[user_index].append(product)
                                cart_quantity.append(qty)
                                cart_amount.append(amnt)
                                print(product," is added to cart list")
                            else:
                                print(product,"is out of stock")
                                
                                #cart_list_price.append(price[index_value])
                            #print(cart_list_price)
                            
                            
                        elif product=="over":
                            break
                        
                        else:
                            print(product," not in the products list")

                elif choose==3:
                    remove_product=input("enter the product to remove from cart:")
                    if remove_product in cart_list:
                        cart_list.remove(remove_product)
                        print(remove_product," is removed from cart list")
                    else:
                        print(remove_product," is not in cart list")

                elif choose==4:
                    print(cart_list)


                elif choose==5:
                        for i in zip(cart_list,cart_quantity,cart_amount):
                            print(f"{i[0]: <15}{i[1]: <7}{i[2]: <7}")
                        print("-"*29)
                        print(" " *14,"Total",sum(cart_amount))
                            
                        
                elif choose==6:
                    print("exit")
                    
                    break
                else:
                    print("thank you for shopping ")
                    
                
                                
        
            


















                
