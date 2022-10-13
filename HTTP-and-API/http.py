
# * HTTP: Hyper Text Transfer Protocol

# * What happens when you enter a URL into the Browser?

# ? 1. DNS(Domain name system) lookup 
# ? 2. Computer makes a REQUEST to a server
# ? 3. Server processes the REQUEST
# ? 4. Server issuesss a RESPONSE

# * So what is a DNS Lookup?

# ? Like a phonebook but for the internet!
# ? The Process: google.com -> DNS Server -> 172.213.9.142
# ? In other words: The destination -> the phonebook -> the (IP) address 
# ? IP = Internet Protocol

# * The request - response cycle

# ? The process: client -> HTTP request -> server -> (sometimes database) -> reponse
# ? In other words: Your computer -> talks to server -> server looks for information -> Sends info back

# * HTTP Headers

# ? Sent with both requests and responses
# ? They provide additional information about the request or response

# * Response Status Codes
# ? 2oo's - Success
# ? 300's - Redirect
# ? 400's - Client Error (You did this!)
# ? 500's - Server Error (Hey! It's not your fault.)