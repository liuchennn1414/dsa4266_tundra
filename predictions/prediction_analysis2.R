library(tidyverse)

A549_replicate5 <- read.csv("A549_directRNA_replicate5_run1.csv")
A549_replicate6 <- read.csv("A549_directRNA_replicate6_run1.csv")
Hct116_replicate3run1 <- read.csv("Hct116_directRNA_replicate3_run1.csv")
Hct116_replicate3run4 <- read.csv("Hct116_directRNA_replicate3_run4.csv")
Hct116_replicate4 <- read.csv("Hct116_directRNA_replicate4_run3.csv")
HepG2_replicate5 <- read.csv("HepG2_directRNA_replicate5_run2.csv")
HepG2_replicate6 <- read.csv("HepG2_directRNA_replicate6_run1.csv")
K562_replicate4 <- read.csv("K562_directRNA_replicate4_run1.csv")
K562_replicate5 <- read.csv("K562_directRNA_replicate5_run1.csv")
K562_replicate6 <- read.csv("K562_directRNA_replicate6_run1.csv")
MCF7_replicate3 <- read.csv("MCF7_directRNA_replicate3_run1.csv")
MCF7_replicate4 <- read.csv("MCF7_directRNA_replicate4_run1.csv")

# Mutate a new column named "label" based on the probability column
A549_replicate5 <- A549_replicate5 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

A549_replicate6 <- A549_replicate6 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

Hct116_replicate3run1 <- Hct116_replicate3run1 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

Hct116_replicate3run4 <- Hct116_replicate3run4 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

Hct116_replicate4 <- Hct116_replicate4 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

HepG2_replicate5 <- HepG2_replicate5 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

HepG2_replicate6 <- HepG2_replicate6 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

K562_replicate4 <- K562_replicate4 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

K562_replicate5 <- K562_replicate5 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

K562_replicate6 <- K562_replicate6 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

MCF7_replicate3 <- MCF7_replicate3 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))

MCF7_replicate4 <- MCF7_replicate4 %>%
  mutate(label = ifelse(probability > 0.5, 1, 0))


# Identify common rows based on both transcript_id and transcript_position
common_rows <- inner_join(MCF7_replicate3,MCF7_replicate4, by = c("transcript_id", "transcript_position"))

# Perform Fisher's exact test on the "label.x" and "label.y" columns
contingency_table <- table(common_rows$label.x, common_rows$label.y)
result <- fisher.test(contingency_table)

# Print the result
print(result)

