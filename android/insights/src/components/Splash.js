import React from 'react'
import { Appbar, Title } from 'react-native-paper'
import { View, StyleSheet, Text } from 'react-native'

const Splash = () => (
 <View style={styles.splash}>
    <Title style={styles.title}><Text style={{color:"yellow", fontWeight:"bold"}}>i</Text> N S <Text style={{color:"yellow", fontWeight:"bold"}}>i</Text> G H T S</Title>
  </View>
 )

export default Splash

const styles = StyleSheet.create({
  splash: {
    backgroundColor: "rgba(21, 22, 24, 1)",
    height: "100%",
    flex: 1,
    alignItems: "center",
    justifyContent: "center"
  },
  title: {
    color: "white",
    fontSize: 30,
    padding: 5
  }
})