import streamlit as st

# Initialize session state for stock
if 'stock' not in st.session_state:
    st.session_state.stock = 100  # Initial stock
    st.session_state.price = 50   # Price per unit
    st.session_state.sold = 0     # Total units sold

# Title
st.title("🛒 Simple Grocery Ledger")

# Display product info
st.subheader("Product: Apple")
st.write(f"Price per unit: ₹{st.session_state.price}")
st.write(f"Current Stock: {st.session_state.stock}")

# Input for selling
sell_quantity = st.number_input("Enter quantity to sell:", min_value=0, step=1)

# Button to sell
if st.button("Sell"):
    if sell_quantity > st.session_state.stock:
        st.error(f"Not enough stock! Only {st.session_state.stock} left.")
    else:
        st.session_state.stock -= sell_quantity
        st.session_state.sold += sell_quantity
        st.success(f"Sold {sell_quantity} Apple(s) successfully!")

# Show Ledger
st.subheader("📋 Ledger Summary")
total_sales = st.session_state.sold * st.session_state.price

st.write(f"Total Units Sold: {st.session_state.sold}")
st.write(f"Stock Remaining: {st.session_state.stock}")
st.write(f"Total Sales: ₹{total_sales}")
