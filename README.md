# Reservation



```
query {
  tables {
    number
    reserved(date: "2020-10-10")
  }
}

mutation {
  createOrder(input: {table: 1, name: "Name", date: "2020-10-10", email: "sh.kiruh@gmail.com"}) {
    errors {
      messages
    }
    order {
      id
    }
  }
}

```