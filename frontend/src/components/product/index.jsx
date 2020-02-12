import React from "react";
import {
  Container,
  Grid,
  Typography,
  Button,
  Paper,
  Box
} from "@material-ui/core";
import "./style.css";
import MessageIcon from "@material-ui/icons/Message";

export default function Product({ product, user }) {
  const { title, description, image } = product || {};

  return (
    <div>
      <Container maxWidth="md">
        <Grid container alignItems="center">
          <Grid item xs={12} md={6} className="product-image">
            <img src={image} alt="" className="display-img" />
          </Grid>
          <Grid item md={2}>
            {null}
          </Grid>
          <Grid item md={4}>
            <ContactInfo user={user}></ContactInfo>
          </Grid>
          <Grid
            item
            container
            md={12}
            direction="column"
            alignItems="center"
            justify="center"
          >
            <Typography variant="h3">{title}</Typography>
            <Typography variant="body1">{description}</Typography>
          </Grid>
        </Grid>
      </Container>
    </div>
  );
}

function ContactInfo({ user }) {
  const { name, telephone, email } = user || {};
  return (
    <Paper className="contact-info" elevation={10}>
      <Typography>Tlf: +47 {telephone}</Typography>
      <Typography>Epost: {email}</Typography>
      <Typography>Navn: {name}</Typography>
      <Button
        component={Box}
        mt={2}
        variant="contained"
        color="primary"
        startIcon={<MessageIcon />}
      >
        Send melding
      </Button>
    </Paper>
  );
}
