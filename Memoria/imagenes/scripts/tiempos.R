library(ggplot2)

# Tiempos de entrenamiento
modelos<-c("AE Fully Connected", "AE FC lotes", "AE LSTM", "Pred. LSTM", "Pred. CNN-LSTM")
tiempos<-c(1250,350,6250,60000,20000)
data<-as.data.frame(cbind(modelos, tiempos))

data$tiempos = as.double(levels(data$tiempos))[data$tiempos]

p.dt<-ggplot(data, aes(x=modelos, y=tiempos, fill=modelos)) +
  geom_bar(stat="identity")+theme_minimal()+theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  labs(title="Tiempos de entrenamiento", x="Modelos", y="Tiempos (s)", fill="Modelos")
ggsave(filename = "tiempos_entrenamiento.png",plot=p.dt, width = 7, height = 7)

# Tiempos de prediccion
modelos<-c("AE Fully Connected", "AE FC lotes", "AE LSTM", "Pred. LSTM", "Pred. CNN-LSTM", "FB LOF", "HBOS", "IForest", "KNN", "LODA", "LOF", "PCA")
tiempos<-c(7.6432,8.1478,9.3564,10.2187,8.5642,498.5435,2.224,48.9014,102.8687,1.5531,106.7117,1.732)
data<-as.data.frame(cbind(modelos, tiempos))

data$tiempos = as.double(levels(data$tiempos))[data$tiempos]

p.dt<-ggplot(data, aes(x=modelos, y=tiempos, fill=modelos)) +
  geom_bar(stat="identity")+theme_minimal()+theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  labs(title="Tiempos de entrenamiento", x="Modelos", y="Tiempos (s)", fill="Modelos")
ggsave(filename = "tiempos_prediccion.png",plot=p.dt, width = 7, height = 7)

# Tiempos de prediccion sin FB LOF
modelos<-c("AE Fully Connected", "AE FC lotes", "AE LSTM", "Pred. LSTM", "Pred. CNN-LSTM", "HBOS", "IForest", "KNN", "LODA", "LOF", "PCA")
tiempos<-c(7.6432,8.1478,9.3564,10.2187,8.5642,2.224,48.9014,102.8687,1.5531,106.7117,1.732)
data<-as.data.frame(cbind(modelos, tiempos))

data$tiempos = as.double(levels(data$tiempos))[data$tiempos]

p.dt<-ggplot(data, aes(x=modelos, y=tiempos, fill=modelos)) +
  geom_bar(stat="identity")+theme_minimal()+theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  labs(title="Tiempos de entrenamiento", x="Modelos", y="Tiempos (s)", fill="Modelos")
ggsave(filename = "tiempos_prediccion2.png",plot=p.dt, width = 7, height = 7)