//code for the arduino mega
void setup() {
    Serial.begin(9600);  // Open Serial (USB) communication with the computer
    Serial1.begin(9600); // Open Serial1 communication (e.g., with another device)
}

void loop() {
    // Check if data is available on Serial1
    while (Serial1.available()) {
        char incomingByte = Serial1.read();  // Read a byte from Serial1
        Serial.write(incomingByte);         // Send it to the computer via Serial
    }
}
