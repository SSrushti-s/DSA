def knapsack(weights, values, capacity):
    """
    Solve the 0/1 knapsack problem using a greedy approach.

    Parameters:
    weights (list): A list of weights for each item.
    values (list): A list of values for each item.
    capacity (int): The maximum weight capacity of the knapsack.

    Returns:
    tuple: A tuple containing the total value and the list of selected items.
    """
    # Calculate value-to-weight ratio for each item
    value_weight_ratio = [(values[i] / weights[i], i) for i in range(len(weights))]
    
    # Sort items by value-to-weight ratio in descending order
    value_weight_ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    selected_items = []
    
    for ratio, index in value_weight_ratio:
        if weights[index] <= capacity:
            # If the item can fit in the knapsack, add it
            capacity -= weights[index]
            total_value += values[index]
            selected_items.append(index)
    
    return total_value, selected_items

if __name__ == "__main__":
    # Example usage
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    
    total_value, selected_items = knapsack(weights, values, capacity)
    print(f"Total value: {total_value}")
    print(f"Selected items: {selected_items}")